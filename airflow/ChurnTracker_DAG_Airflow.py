import pandas as pd
import numpy as np
import psycopg2 as db
from sqlalchemy import create_engine
from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def load_data():
    # String koneksi untuk PostgreSQL
    conn_string = "dbname='finalproject' host='postgres' user='airflow' password='airflow'"
    conn = db.connect(conn_string)
    # Membaca data dari tabel 'table_fp' ke dalam DataFrame
    df = pd.read_sql("select * from table_fp", conn)
    df.to_csv('/opt/airflow/dags/final_project_data_raw.csv', index=False)