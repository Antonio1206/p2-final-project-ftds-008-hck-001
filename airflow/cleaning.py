import pandas as pd

def clean_data():
    data = pd.read_csv('/opt/airflow/data/P2M3_antonius_daeneg_data_raw2.csv')

    # Mapping kolom
    kolom_mapping = {
        'brand': 'brand',
        'model': 'model',
        'sd_card': 'sd_card',
        'main_camera': 'main_camera',
        'resolution': 'resolution',
        'display': 'display',
        'sim_card': 'sim_card',
        'os': 'Sistem_operasi',
        'color': 'color',
        'region': 'region',
        'location': 'location',
        'screen_size(inch)': 'screen_size',
        'battery(mAh)': 'battery',
        'storage(GB)': 'storage',
        'ram(GB)': 'ram',
        'selfie_camera(MP)': 'selfie_camera',
        'price(¢)': 'price'
    }

    # Mengganti nama kolom
    data.rename(columns=kolom_mapping, inplace=True)

    # Menghapus duplikat
    data = data.drop_duplicates()

    # Menghapus nilai NULL
    data = data.dropna()

    # Mengubah tipe data kolom 'price' menjadi int
    data['price'] = data['price'].astype(int)

    # Simpan data yang sudah bersih ke dalam file "data_bersih.csv"
    data.to_csv('/opt/airflow/data/P2M3_antonius_daeng_data_clean.csv', index=False)
