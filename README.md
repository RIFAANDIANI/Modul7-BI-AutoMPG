🚗 Tugas BI Modul 7: Interactive Auto-MPG Dashboard
Deskripsi Proyek
Proyek ini adalah implementasi Business Intelligence (BI) untuk Modul 7 Mata Kuliah Data Science. Dashboard ini dibangun secara programmatic menggunakan Python untuk menganalisis dataset Auto-mpg dan memberikan insight interaktif terkait efisiensi bahan bakar kendaraan.

Pertanyaan Analisis yang Dijawab:
P1 (Interaktif): Bagaimana hubungan antara weight dan mpg (difilter berdasarkan Origin dan Horsepower)?

P2 (Tren): Bagaimana tren rata-rata mpg dari tahun ke tahun?

P3 (Komparasi): Apakah ada perbedaan rata-rata mpg berdasarkan jumlah cylinders?

🚀 Cara Menjalankan Dashboard
Dashboard ini dibuat menggunakan Panel dan Hvplot dan harus dijalankan dari terminal menggunakan perintah panel serve.

1. Persyaratan Sistem
Pastikan Anda telah menginstal Python (disarankan versi 3.9+) dan mengaktifkan virtual environment (.venv).

2. Instalasi Dependensi
Instal semua library yang diperlukan yang tercantum dalam file requirements.txt:

Bash

pip install -r requirements.txt
3. Struktur File
Pastikan root direktori proyek Anda memiliki struktur berikut:

MODUL 7/
├── .venv/                   # Virtual Environment
├── auto-mpg.data            # File dataset utama
├── dashboard_mpg.py         # Kode Python Dashboard (Panel/Hvplot)
└── requirements.txt         # Daftar Library (Pandas, Panel, hvplot, holoviews)
4. Menjalankan Server
Jalankan script Python sebagai aplikasi web menggunakan Panel:


panel serve dashboard_mpg.py --show --port 5006   

Setelah dijalankan, buka link berikut di browser Anda:

http://localhost:5006/dashboard_mpg

💡 Insight Kunci (Ringkasan)
Dashboard ini mengkonfirmasi beberapa insight penting dari data kendaraan:

Korelasi Negatif: Terdapat korelasi kuat bahwa peningkatan berat kendaraan (weight) menyebabkan penurunan efisiensi bahan bakar (MPG). Filter interaktif membuktikan bahwa strategi desain regional (misalnya, desain ringan pada mobil Eropa/Jepang) adalah penentu efisiensi terbesar.

Tren Efisiensi: Rata-rata MPG mobil secara keseluruhan menunjukkan peningkatan stabil dari tahun 1970 hingga 1982.

Efek Mesin: Mobil 4 silinder adalah yang paling efisien, sementara mobil 8 silinder adalah yang paling boros.