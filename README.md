# 🏦 FinRisk AI: Smart Credit Scoring & Risk Analysis

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![TailwindCSS](https://img.shields.io/badge/UI-Tailwind--CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)

**FinRisk AI** adalah aplikasi web berbasis Machine Learning yang dirancang untuk membantu institusi keuangan memprediksi kelayakan kredit nasabah secara instan. Menggunakan algoritma Random Forest Classifier, sistem ini menganalisis profil risiko berdasarkan pendapatan, usia, tanggungan, dan riwayat BI Checking.

## ✨ Fitur Unggulan
- **ML-Powered Prediction:** Klasifikasi risiko (Low vs High) dengan tingkat akurasi tinggi.
- **Dynamic UI/UX:** Antarmuka modern menggunakan Tailwind CSS dengan efek Glassmorphism.
- **Currency Formatter:** Input pendapatan otomatis terformat (Contoh: 5.000.000) untuk kenyamanan user.
- **Interactive Credit Score Slider:** Memudahkan input nilai BI Checking dengan rentang 300 - 850.
- **Business Logic Integration:** Dilengkapi dengan aturan bisnis tambahan untuk memastikan hasil prediksi logis dan realistis.

## 🛠️ Stack Teknologi
- **Backend:** Flask (Python)
- **Machine Learning:** Scikit-Learn (Random Forest), Joblib, Pandas, NumPy
- **Frontend:** HTML5, JavaScript (Vanilla), Tailwind CSS
- **Deployment Ready:** Port-optimized (Avoids macOS AirPlay conflicts)

## 📂 Struktur Proyek
- app.py: Server Flask & Logika Integrasi Model.
- train_model.py: Script untuk pelatihan model Machine Learning.
- buat_csv.py: Generator dataset sintetik dengan logika risiko realistis.
- templates/index.html: Dashboard antarmuka pengguna.
- credit_model.pkl: Model yang sudah terlatih (Binary format).

## ⚙️ Cara Menjalankan Secara Lokal

1. Clone Repository:
   git clone https://github.com/reithvxz/finrisk-ai-credit-scoring.git
   cd finrisk-ai-credit-scoring

2. Instal Dependensi:
   pip install flask pandas scikit-learn joblib

3. Persiapkan Model (Jika ingin melatih ulang):
   python buat_csv.py
   python train_model.py

4. Jalankan Aplikasi:
   python app.py

Aplikasi akan berjalan di http://127.0.0.1:5001 (Optimized for Mac).

---
**Developed by Okan Athallah Maredith**
Technology & Data Science Student @ Universitas Airlangga
