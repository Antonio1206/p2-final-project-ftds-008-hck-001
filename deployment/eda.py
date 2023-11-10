import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

def run():
    # st.title('Selamat Datang Di Halaman EDA!')    
    plot_selection = st.sidebar.selectbox(label='Choose',options=["Churn and Not-Churn Customers Percentage", "Distribution of Total Charges by Churn", "Distribution of Tenure by Churn", "Customer information vs Target Variable (Churn)", "Support services vs Target Variable (Churn)"])
    
    st.title('ChurnTracker EDA')
    # # Memanggil data csv
    st.caption('Data CSV')
    data = pd.read_csv('dataset_fpfix.csv')
    # st.dataframe(data)
    # Menampilkan 5 data teratas
    st.caption('Data Head')
    st.table(data.head(5))
    # # Menampilkan 5 data terbawah
    # st.caption('Data Tail')
    # st.table(data.tail(5))

        # Function to create Plot 1
    def create_plot_1(data):
        st.title('Churn and Not-Churn Customers Percentage')
        with st.expander('Explanation'):
            st.text('''
                "Hanya 26.59% pelanggan yang beralih ke provider lainnya, Tentunya ini bukanlah
                angka yang mengkawatirkan dikarenakan masih ada 3/4 dari keseluruhan pelanggan 
                yang masih setia terhadap perusahaan, Akan tetapi akan lebih baik kita dapat 
                mencegah 1/4 dari total pelanggan untuk berpaling ke provider lainnya, dengan 
                harapan dapat meningkatkan pendapatan perusahaan kedepannya."
            ''')
        image = Image.open('p1.png')
        st.image(image, caption='chart')


    def create_plot_2(data):
        st.title('Distribution of Total Charges by Churn')
        with st.expander('Explanation'):
            st.text('''
                "Peluang pelanggan untuk beralih ke penyedia layanan lain cenderung meningkat
                seiring dengan kenaikan tagihan bulanan, terutama pada rentang tagihan $60-$120.
                Namun, paradoksnya, semakin besar total tagihan, semakin kecil kemungkinan 
                pelanggan untuk beralih, yang mungkin dipengaruhi oleh faktor waktu penggunaan."
            ''')
        image = Image.open('p2.png')
        st.image(image, caption='chart2')

    def create_plot_3(data):
        st.title('Distribution of Tenure by Churn')
        with st.expander('Explanation'):
            st.text('''
                "Pelanggan baru memiliki kecenderungan yang lebih tinggi untuk beralih 
                dibandingkan dengan pelanggan lama. Oleh karena itu, diperlukan perlakuan
                khusus atau strategi pemasaran yang lebih intensif untuk memastikan retensi
                pelanggan baru."
            ''')
        image = Image.open('p3.png')
        st.image(image, caption='chart3')

    def create_plot_4(data):
        st.title('Customer information vs Target Variable (Churn)')
        with st.expander('Explanation'):
            st.text('''
                "Meskipun jenis kelamin memiliki pengaruh yang minim terhadap kecenderungan 
                pelanggan untuk beralih atau tidak, terlihat perbedaan nilai churn yang kecil 
                antara laki-laki dan perempuan. Sementara itu, customer yang berumur tua cenderung
                lebih setia dalam mempertahankan penggunaan layanan perusahaan, menunjukkan 
                kestabilan dan kesetiaan dalam jangka waktu yang lebih lama."
            ''')
        image = Image.open('p4.png')
        st.image(image, caption='chart4')

    def create_plot_5(data):
        st.title('Support services vs Target Variable (Churn)')
        with st.expander('Explanation'):
            st.text('''
                "Pelanggan yang menggunakan layanan tambahan cenderung memiliki peluang beralih 
                yang lebih kecil. Ini mungkin disebabkan oleh keberadaan layanan tambahan sebagai 
                bentuk backup, memberikan rasa aman kepada pelanggan jika terjadi sesuatu yang tidak 
                diinginkan dan dengan demikian, mengurangi kecenderungan untuk beralih."
            ''')
        image = Image.open('p5.png')
        st.image(image, caption='chart5')


    # Display the selected plot
    if plot_selection == "Churn and Not-Churn Customers Percentage":
        create_plot_1(data)
    elif plot_selection == "Distribution of Total Charges by Churn":
        create_plot_2(data)
    elif plot_selection == "Distribution of Tenure by Churn":
        create_plot_3(data)
    elif plot_selection == "Customer information vs Target Variable (Churn)":
        create_plot_4(data)
    elif plot_selection == "Support services vs Target Variable (Churn)":
        create_plot_5(data)
