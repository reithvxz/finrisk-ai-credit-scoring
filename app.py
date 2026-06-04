from flask import Flask, render_template, request
import joblib
import numpy as np
import locale

# Setup locale for formatting currency (optional, we can just use manual formatting)
app = Flask(__name__)

# Load model
model = joblib.load('credit_model.pkl')

def format_rupiah(angka):
    return f"Rp {int(angka):,}".replace(",", ".")

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    
    if request.method == 'POST':
        try:
            # Ambil data & konversi ke float
            pendapatan = float(request.form['pendapatan'])
            usia = float(request.form['usia'])
            tanggungan = float(request.form['tanggungan'])
            skor_lama = float(request.form['skor_lama'])
            cicilan = float(request.form['cicilan'])
            rumah = float(request.form['rumah'])
            plafon = float(request.form['plafon'])
            tenor = float(request.form['tenor'])
            
            features = [pendapatan, usia, tanggungan, skor_lama, cicilan, rumah, plafon, tenor]
            final_features = [np.array(features)]
            
            # Prediksi dengan AI
            prediction = model.predict(final_features)
            # Probabilitas Aman (Kelas 0)
            prob_safe = model.predict_proba(final_features)[0][0] * 100
            
            # ----------------------------------------------------
            # ADVANCED RULE ENGINE (Sistem Kredit Profesional)
            # ----------------------------------------------------
            
            # 1. Hitung Cicilan Per Bulan (Bunga Flat Estimasi 1.5% per bulan)
            estimasi_bunga_per_bulan = 0.015
            cicilan_pokok = plafon / tenor
            cicilan_bunga = plafon * estimasi_bunga_per_bulan
            cicilan_total = cicilan_pokok + cicilan_bunga
            
            # 2. Hitung Debt-to-Income (DTI) Ratio
            dti = cicilan_total / pendapatan if pendapatan > 0 else 1.0
            dti_percent = dti * 100
            
            # 3. Hitung Rekomendasi Plafon Maksimal (Batas DTI 40%)
            max_cicilan_allowable = pendapatan * 0.40
            max_plafon = max_cicilan_allowable / ((1/tenor) + estimasi_bunga_per_bulan)
            
            # 4. HARD RULES (Filter Ketat)
            hard_reject_reasons = []
            
            if dti_percent > 45:
                hard_reject_reasons.append(f"Debt-to-Income Ratio terlalu tinggi ({dti_percent:.1f}%). Maksimal yang disarankan adalah 40%.")
                prob_safe = min(prob_safe, 15.0) # Drop confidence
                prediction[0] = 1
                
            if cicilan == 0: # Ada riwayat macet
                hard_reject_reasons.append("Terdapat riwayat kredit macet (BI Checking Buruk).")
                prob_safe = min(prob_safe, 10.0)
                prediction[0] = 1
                
            if skor_lama < 400:
                hard_reject_reasons.append(f"Skor Kredit terlalu rendah ({int(skor_lama)}).")
                prob_safe = min(prob_safe, 25.0)
                prediction[0] = 1
                
            # Keputusan Akhir
            if prediction[0] == 0 and prob_safe > 50:
                status = "DISETUJUI"
                risk_level = "LOW RISK"
                color_class = "emerald"
                color_hex = "#10b981"
            else:
                status = "DITOLAK"
                risk_level = "HIGH RISK"
                prob_safe = 100 - prob_safe if prob_safe > 50 else prob_safe # pastikan confidence penolakan
                color_class = "rose"
                color_hex = "#f43f5e"
                
            result = {
                'status': status,
                'risk_level': risk_level,
                'probability': f"{prob_safe:.1f}%",
                'color_class': color_class,
                'color_hex': color_hex,
                'dti_percent': f"{dti_percent:.1f}%",
                'cicilan_per_bulan': format_rupiah(cicilan_total),
                'max_plafon': format_rupiah(max_plafon) if max_plafon > 0 else "Rp 0",
                'reasons': hard_reject_reasons
            }
            
        except Exception as e:
            result = {
                'status': 'ERROR',
                'error_msg': str(e),
                'color_class': 'amber',
                'color_hex': '#f59e0b'
            }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)