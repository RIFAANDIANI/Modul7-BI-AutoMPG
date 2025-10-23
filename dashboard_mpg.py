import pandas as pd
import hvplot.pandas
import panel as pn
import holoviews as hv

# Aktifkan ekstensi Panel
pn.extension()
hv.extension('bokeh')

# --------------------------
# 1. MEMUAT DAN MEMBERSIHKAN DATA
# --------------------------

# Tentukan nama file yang benar
file_data = 'auto-mpg.data'

# Tentukan nama kolom (dibutuhkan karena file .data tanpa header)
column_names = [
    'mpg', 'cylinders', 'displacement', 'horsepower', 
    'weight', 'acceleration', 'model year', 'origin', 'car name'
]

# Muat Dataset dengan penyesuaian untuk file .data
try:
    df = pd.read_csv(
        file_data, 
        delim_whitespace=True,      # Menggunakan spasi sebagai pemisah
        header=None,                # File tidak memiliki header
        names=column_names,         # Menggunakan nama kolom manual
        na_values='?'               # Menangani missing values
    )
    print(f"✓ Data berhasil dimuat: {len(df)} baris")
except FileNotFoundError:
    print(f"Error: Pastikan file '{file_data}' ada di direktori kerja.")
    raise SystemExit("File dataset tidak ditemukan. Pastikan nama file dan lokasi sudah benar.")

# Pre-processing Data Lanjutan
df = df.dropna() # Menghapus baris dengan missing value

# Mengubah tipe data untuk analisis/filter
df['horsepower'] = df['horsepower'].astype(float)
df['cylinders'] = df['cylinders'].astype(str)
df['model year'] = df['model year'].astype(str)

# PERBAIKAN PENTING: Mapping origin dari kode numerik ke label deskriptif
origin_mapping = {
    1: 'USA',
    2: 'Europe',
    3: 'Japan'
}
df['origin'] = df['origin'].map(origin_mapping)

print(f"✓ Data setelah cleaning: {len(df)} baris")
print(f"✓ Origin mapping: {df['origin'].value_counts().to_dict()}")

# --------------------------
# 2. DEFINISI WIDGET INTERAKTIF (Minimal 2 Widget)
# --------------------------

# Widget 1: Dropdown untuk memilih Origin (sekarang dengan label deskriptif)
origin_options = sorted(list(df['origin'].unique()))
origin_widget = pn.widgets.Select(
    name='Pilih Asal Mobil (Origin)', 
    options=origin_options, 
    value=origin_options[0]
)

# Widget 2: Range Slider untuk memfilter Horsepower
hp_min = int(df['horsepower'].min())
hp_max = int(df['horsepower'].max())
hp_slider = pn.widgets.RangeSlider(
    name='Rentang Horsepower (HP)', 
    start=hp_min, 
    end=hp_max, 
    value=(hp_min, hp_max)
)

# --------------------------
# 3. FUNGSI INTERAKTIF (@pn.depends)
#    Menjawab Pertanyaan 1: Bagaimana hubungan antara weight dan mpg?
# --------------------------

@pn.depends(origin_widget.param.value, hp_slider.param.value)
def interactive_scatter(origin, hp_range):
    """
    Fungsi ini memfilter data berdasarkan Widget Origin dan Horsepower,
    kemudian menampilkan Scatter Plot interaktif (Weight vs MPG).
    """
    min_hp, max_hp = hp_range

    filtered_df = df[
        (df['origin'] == origin) & 
        (df['horsepower'] >= min_hp) & 
        (df['horsepower'] <= max_hp)
    ]
    
    if len(filtered_df) == 0:
        return pn.pane.Markdown("### ⚠️ Tidak ada data dengan filter ini")

    # Membuat Scatter Plot (Weight vs MPG)
    # PERBAIKAN: Gunakan marker_size (bukan size) untuk kompatibilitas
    scatter_plot = filtered_df.hvplot.scatter(
        x='weight',
        y='mpg',
        c='model year',  # Color berdasarkan model year
        marker='circle',
        alpha=0.7,
        cmap='Category20',  # Color palette
        title=f'Weight vs MPG untuk Origin: {origin} (HP: {min_hp}-{max_hp})',
        height=400,
        width=700,
        responsive=True,
        hover_cols=['car name', 'horsepower', 'model year', 'cylinders'],
        xlabel='Weight (lbs)',
        ylabel='MPG (Miles Per Gallon)',
        legend='top_right'
    )
    
    return scatter_plot

# --------------------------
# 4. VISUALISASI STATIS
#    Menjawab Pertanyaan 2 & 3
# --------------------------

# Pertanyaan 2: Bagaimana tren rata-rata mpg dari tahun ke tahun? (Line Plot)
mean_mpg_year = df.groupby('model year')['mpg'].mean().reset_index()
trend_plot = mean_mpg_year.hvplot.line(
    x='model year',
    y='mpg',
    title='Tren Rata-Rata MPG dari Tahun ke Tahun',
    height=350,
    width=500,
    responsive=True,
    hover_cols=['mpg'],
    xlabel='Tahun Model',
    ylabel='Rata-Rata MPG',
    line_width=3,
    color='orange'
)

# Pertanyaan 3: Apakah ada perbedaan rata-rata mpg berdasarkan cylinders? (Bar Plot)
mean_mpg_cyl = df.groupby('cylinders')['mpg'].mean().sort_values(ascending=True).reset_index()
bar_plot = mean_mpg_cyl.hvplot.bar(
    x='cylinders',
    y='mpg',
    title='Rata-Rata MPG berdasarkan Jumlah Cylinders',
    height=350,
    width=500,
    responsive=True,
    hover_cols=['mpg'],
    xlabel='Jumlah Cylinders',
    ylabel='Rata-Rata MPG',
    color='steelblue',
    invert_axes=True
)

# --------------------------
# 5. MENYUSUN LAYOUT DASHBOARD (Panel)
# --------------------------

# Header Dashboard
title_header = pn.pane.Markdown(
    '# 🚗 Dashboard Analisis Auto-MPG',
    sizing_mode='stretch_width'
)

description = pn.pane.Markdown(
    """
    Dashboard ini menyajikan analisis interaktif terhadap **Auto-MPG dataset**.
    
    **Cara Penggunaan:**
    - Gunakan filter **Origin** dan **Horsepower** di sidebar untuk memvisualisasikan 
      hubungan **Weight** dan **MPG** secara dinamis
    - Dataset mencakup mobil dari USA, Europe, dan Japan (1970-1982)
    """,
    sizing_mode='stretch_width'
)

# Layout Sidebar (Interaktif)
sidebar_content = pn.Column(
    title_header,
    description,
    pn.layout.Divider(),
    pn.pane.Markdown('### 🎛️ Filter Interaktif'),
    origin_widget,
    hp_slider,
    pn.layout.Divider(),
    pn.pane.Markdown(f'**📊 Statistik Dataset:**'),
    pn.pane.Markdown(f'- Total: **{len(df)}** mobil'),
    pn.pane.Markdown(f'- USA: **{len(df[df["origin"]=="USA"])}** mobil'),
    pn.pane.Markdown(f'- Europe: **{len(df[df["origin"]=="Europe"])}** mobil'),
    pn.pane.Markdown(f'- Japan: **{len(df[df["origin"]=="Japan"])}** mobil'),
    sizing_mode='stretch_width'
)

# Layout Main (Statis & Interaktif)
main_content = pn.Column(
    pn.pane.Markdown('## 📊 Visualisasi Statis untuk Insight Tambahan'),
    pn.Row(
        pn.Column(
            pn.pane.Markdown('### P2: Tren MPG Tahunan'),
            trend_plot
        ),
        pn.Column(
            pn.pane.Markdown('### P3: Perbedaan MPG per Cylinders'),
            bar_plot
        ),
        sizing_mode='stretch_width'
    ),
    pn.layout.Divider(),
    pn.pane.Markdown('## 📈 P1: Hubungan Weight vs MPG (Plot Interaktif)'),
    pn.pane.Markdown(
        """
        **Insight:** Plot ini menunjukkan korelasi negatif antara berat kendaraan (weight) 
        dan efisiensi bahan bakar (MPG). Semakin berat mobil, semakin rendah MPG-nya.
        """
    ),
    interactive_scatter,
    sizing_mode='stretch_width'
)

# Gabungkan semua komponen ke dalam template Panel
dashboard = pn.template.FastListTemplate(
    title='Tugas BI Modul 7 - Auto-MPG Dashboard',
    sidebar=[sidebar_content],
    main=[main_content],
    header_background='#0077b6',
    accent_base_color='#0077b6',
    sidebar_width=320,
    theme='default'
)

# --------------------------
# 6. MENJADIKAN APLIKASI WEB (SERVE)
# --------------------------

# Debug info
print("\n" + "="*60)
print("✓ Dashboard siap dijalankan!")
print("✓ Jalankan dengan: panel serve dashboard_mpg.py --show")
print("="*60 + "\n")

dashboard.servable()