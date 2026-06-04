import pandas as pd
import numpy as np
import random

def generate_credit_data(num_records=2000):
    np.random.seed(42)
    random.seed(42)
    
    data = []
    
    for _ in range(num_records):
        pendapatan_bulanan = np.random.randint(3000000, 50000000)
        usia = np.random.randint(21, 60)
        jumlah_tanggungan = np.random.randint(0, 5)
        skor_kredit_lama = np.random.randint(300, 850)
        cicilan_lancar = np.random.choice([0, 1], p=[0.3, 0.7])
        status_rumah = np.random.choice([0, 1, 2]) # 0: Sewa, 1: Milik Sendiri, 2: KPR
        
        plafon_kredit = np.random.randint(5000000, 500000000)
        # Bikin kelipatan 1 juta
        plafon_kredit = (plafon_kredit // 1000000) * 1000000
        
        tenor_bulan = np.random.choice([12, 24, 36, 48, 60])
        
        # Calculate DTI
        estimasi_bunga_per_bulan = 0.015 # 1.5% per bulan
        cicilan_pokok = plafon_kredit / tenor_bulan
        cicilan_bunga = plafon_kredit * estimasi_bunga_per_bulan
        cicilan_total = cicilan_pokok + cicilan_bunga
        
        dti = cicilan_total / pendapatan_bulanan
        
        # Penentuan Target Default (1 = Macet/Ditolak, 0 = Lancar/Disetujui)
        risk_score = 0
        
        if dti > 0.45:
            risk_score += 4
        elif dti > 0.35:
            risk_score += 2
            
        if skor_kredit_lama < 500:
            risk_score += 3
        elif skor_kredit_lama < 650:
            risk_score += 1
            
        if cicilan_lancar == 0:
            risk_score += 4
            
        if jumlah_tanggungan >= 3 and pendapatan_bulanan < 10000000:
            risk_score += 2
            
        if status_rumah == 0:
            risk_score += 1
            
        # Add some random noise
        risk_score += np.random.uniform(-1, 1)
        
        # Threshold for default
        target_default = 1 if risk_score >= 5 else 0
        
        data.append([
            pendapatan_bulanan, usia, jumlah_tanggungan, skor_kredit_lama,
            cicilan_lancar, status_rumah, plafon_kredit, tenor_bulan, target_default
        ])
        
    df = pd.DataFrame(data, columns=[
        'pendapatan_bulanan', 'usia', 'jumlah_tanggungan', 'skor_kredit_lama',
        'cicilan_lancar', 'status_rumah', 'plafon_kredit', 'tenor_bulan', 'target_default'
    ])
    
    df.to_csv('credit_data.csv', index=False)
    print("✅ Berhasil membuat credit_data.csv dengan 2000 baris dan fitur baru!")

if __name__ == "__main__":
    generate_credit_data()
