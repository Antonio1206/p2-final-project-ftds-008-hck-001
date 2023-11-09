import pandas as pd
import psycopg2

def extract_data():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="airflow",
        password="airflow"
    )
    query = "SELECT * FROM final_projek"
    data = pd.read_sql(query, conn)
    conn.close()

    # Simpan data ke dalam file CSV "data_kotor.csv"
    data.to_csv('/opt/airflow/data/data_kotor.csv', index=False)