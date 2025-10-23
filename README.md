# 🚗 BI-Dashboard-AutoMPG-Python: Tugas Modul 7

Proyek ini adalah implementasi **Business Intelligence (BI)** untuk penugasan Modul 7 Mata Kuliah Data Science, berfokus pada pembangunan *dashboard* interaktif berbasis kode (*programmatic dashboard*) menggunakan Python. Dashboard ini menganalisis dataset `Auto-mpg` untuk memberikan *insight* terkait efisiensi bahan bakar kendaraan.

---

## 🎯 Pertanyaan Analisis yang Dijawab

1.  **P1 (Interaktif):** Bagaimana hubungan antara *weight* dan *mpg* (difilter berdasarkan *Origin* dan *Horsepower*)?
2.  **P2 (Tren):** Bagaimana tren rata-rata *mpg* dari tahun ke tahun?
3.  **P3 (Komparasi):** Apakah ada perbedaan rata-rata *mpg* berdasarkan jumlah *cylinders*?

---

## 💡 Pemaparan Insight Kunci

| Pertanyaan | Visualisasi | Insight Kunci |
| :--- | :--- | :--- |
| **P1** | Scatter Plot + Widget | **Korelasi Negatif Kuat:** Terdapat korelasi negatif yang kuat antara berat mobil dan *MPG*. Mobil **Eropa/Jepang** cenderung lebih efisien (ringan) daripada mobil **USA** (berat). |
| **P2** | Line Plot | **Tren Peningkatan Efisiensi:** Rata-rata *MPG* secara keseluruhan menunjukkan **peningkatan stabil** dari tahun 1970 hingga 1982. |
| **P3** | Bar Plot | **Faktor Silinder Kritis:** Mobil **4 silinder** (dan 3 silinder) adalah yang **paling efisien**, sementara mobil **8 silinder** memiliki rata-rata *MPG* terendah. |

---

## 🛠️ Tools dan Cara Menjalankan

### File Wajib di Repositori:
1.  `dashboard_mpg.py` (Kode Panel/Hvplot)
2.  `auto-mpg.data` (Dataset)
3.  `requirements.txt` (Dependencies: `pandas`, `hvplot`, `panel`, `holoviews`)

### Langkah-langkah Eksekusi:

1.  **Instalasi Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Jalankan Server Dashboard:**
    ```bash
    panel serve dashboard_mpg.py --show --port 5006
    ```

3.  **Akses:** Dashboard akan otomatis terbuka di *web browser* Anda.

---

## Kontak

* **Dibuat oleh:** [Nama Lengkap Anda]
* **Keperluan:** Tugas Akademis Modul 7 Data Science