from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load('credit_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = None
    probability = None
    color = None
    
    if request.method == 'POST':
        try:
            # Ambil data & konversi ke float
            features = [
                float(request.form['pendapatan']),
                float(request.form['usia']),
                float(request.form['tanggungan']),
                float(request.form['skor_lama']),
                float(request.form['cicilan']),
                float(request.form['rumah'])
            ]
            
            final_features = [np.array(features)]
            
            # Prediksi
            prediction = model.predict(final_features)
            # Ambil probabilitas untuk kelas 0 (Aman)
            prob_safe = model.predict_proba(final_features)[0][0] * 100
            
            # LOGIKA FILTER TAMBAHAN (Hard Rule)
            # Biar AI gak bego: Kalau pendapatan < 3jt & tanggungan > 2, OTOMATIS TOLAK
            if features[0] < 3000000 and features[2] > 2:
                prediction[0] = 1
                prob_safe = 15.0 # Paksa drop confidence-nya

            if prediction[0] == 0 and prob_safe > 50:
                prediction_text = "DISETUJUI (LOW RISK)"
                color = "#10b981" # Emerald Green
            else:
                prediction_text = "DITOLAK (HIGH RISK)"
                prob_safe = 100 - prob_safe if prob_safe > 50 else prob_safe
                color = "#ef4444" # Red
                
            probability = f"{prob_safe:.2f}%"
            
        except Exception as e:
            prediction_text = f"Error: {e}"
            color = "#f59e0b"

    return render_template('index.html', 
                           prediction_text=prediction_text, 
                           probability=probability, 
                           color=color)

if __name__ == '__main__':
    # Kita pindah ke port 5001 biar gak tabrakan sama AirPlay Mac
    app.run(debug=True, port=5001)