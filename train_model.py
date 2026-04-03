import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# 1. Load data terbaru yang sudah "Galak" (Logika Realistis)
try:
    df = pd.read_csv('credit_data.csv')
    print("📂 Dataset 'credit_data.csv' berhasil dimuat.")
except FileNotFoundError:
    print("❌ Error: File 'credit_data.csv' tidak ada. Jalankan buat_csv.py dulu!")
    exit()

# 2. Pisahkan Fitur (X) dan Target (y)
X = df.drop('target_default', axis=1)
y = df['target_default']

# 3. Bagi data (80% Latihan, 20% Ujian)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Inisialisasi Model Random Forest
# Kita pakai n_estimators=200 supaya lebih teliti dalam nolak orang
model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)

# 5. Proses Belajar (Training)
print("🤖 AI sedang mempelajari pola risiko kredit... Mohon tunggu.")
model.fit(X_train, y_train)

# 6. Evaluasi (Cek Seberapa Pinter AI-nya)
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Training Selesai! Akurasi Model: {acc:.2f}")

# 7. Simpan hasil belajar ke file .pkl
joblib.dump(model, 'credit_model.pkl')
print("💾 Model 'credit_model.pkl' telah diperbarui dan siap digunakan di app.py!")