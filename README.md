# 🏦 FinRisk AI: Smart Credit Scoring & Risk Analysis

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![TailwindCSS](https://img.shields.io/badge/UI-Tailwind--CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)

**FinRisk AI** adalah aplikasi web berbasis Machine Learning yang dirancang untuk membantu institusi keuangan memprediksi kelayakan kredit nasabah secara instan. Menggunakan algoritma Random Forest Classifier dan Rule Engine tingkat lanjut, sistem ini menganalisis profil risiko secara komprehensif.

## ✨ Fitur Unggulan
- **ML-Powered Prediction:** Klasifikasi risiko kredit dengan tingkat akurasi tinggi menggunakan model Random Forest yang dilatih secara realistis.
- **Advanced Rule Engine (DTI Analysis):** Mengkalkulasi Debt-to-Income (DTI) secara otomatis berdasarkan Plafon dan Tenor untuk simulasi limit kredit profesional.
- **Rekomendasi Max Plafon:** Sistem otomatis memberikan saran batas kredit maksimal yang aman berdasarkan standar DTI 40%.
- **Premium Full-Screen UI/UX:** Antarmuka modern, luas, dan padat informasi menggunakan Tailwind CSS dengan efek Glassmorphism premium.
- **Interactive Credit Score & Currency Formatter:** Format Rupiah otomatis dan Slider interaktif untuk simulasi data pengguna yang mudah.

## 🛠️ Stack Teknologi
- **Backend:** Flask (Python)
- **Machine Learning:** Scikit-Learn (Random Forest), Joblib, Pandas, NumPy
- **Frontend:** HTML5, JavaScript (Vanilla), Tailwind CSS
- **Deployment Ready:** Port-optimized (Avoids macOS AirPlay conflicts)

## 📂 Struktur Proyek
- `app.py`: Server Flask & Logika Integrasi Model beserta Advanced Rule Engine (DTI).
- `generate_data.py`: Generator dataset sintetik dengan logika risiko dan fitur lengkap (Plafon, Tenor, dll).
- `train_model.py`: Script untuk melatih ulang model Machine Learning berdasarkan dataset terbaru.
- `templates/index.html`: Dashboard antarmuka pengguna premium.
- `credit_model.pkl`: Model yang sudah terlatih (Binary format).

## ⚙️ Cara Menjalankan Secara Lokal

1. Clone Repository:
```bash
git clone https://github.com/reithvxz/finrisk-ai-credit-scoring.git
cd finrisk-ai-credit-scoring
```

2. Instal Dependensi:
```bash
pip install flask pandas numpy scikit-learn joblib
```

3. Persiapkan Model (Jika ingin melatih ulang dari awal):
```bash
python generate_data.py
python train_model.py
```

4. Jalankan Aplikasi:
```bash
python app.py
```

Aplikasi akan berjalan di http://127.0.0.1:5001 (Optimized for Mac).

---
**Developed by Okan Athallah Maredith**
Technology & Data Science Student @ Universitas Airlangga
