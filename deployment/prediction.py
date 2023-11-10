import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt


if 'all_data' not in st.session_state:
     st.session_state.all_data = pd.DataFrame()

with open("finale.pkl", "rb") as file1:
    classification_pipeline = pickle.load(file1)

with open("finaleclustering.pkl", "rb") as file2:
    clustering_pipeline = pickle.load(file2)

def run():
    st.title('Cluster Prediction')
    # Manual input
    tenure = st.number_input(label="Since when did the customer become a valued customer with us?", min_value=1, max_value=50, key=1)
    monthly_charges = st.number_input(label="What is the amount the customer invests monthly in our services?", min_value=10, max_value=200, key=2)
    # total_charges = st.number_input(label="What is the total investment the customer has made in our services so far?", min_value=10, max_value=10000, key=3)
    num_tech_tickets = st.number_input(label="How many technical support tickets has the customer raised?", min_value=1, max_value=8, key=4)
    senior_citizen = st.number_input(label="Is the customer a senior citizen? (1 for Yes, 0 for No)", min_value=0, max_value=1, key=5)
    partner = st.radio("Does the customer have a partner?", ["Yes", "No"], key=6)
    dependents = st.radio("Does the customer have dependents?", ["Yes", "No"], key=7)
    contract = st.radio("What is the customer's current contract type?", ["Month-to-month", "One year", "Two year"], key=8)
    online_security = st.radio("Does the customer have online security?", ["Yes", "No"], key=9)
    online_backup = st.radio("Does the customer have online backup?", ["Yes", "No"], key=10)
    device_protection = st.radio("Does the customer have device protection?", ["Yes", "No"], key=11)
    tech_support = st.radio("Does the customer have tech support?", ["Yes", "No"], key=12)


    data_inf = {
        'tenure': tenure,
        'monthly_charges': monthly_charges,
        'total_charges': tenure*monthly_charges,
        'num_tech_tickets': num_tech_tickets,
        'senior_citizen': senior_citizen,
        'partner': partner,
        'dependents': dependents,
        'contract': contract,
        'online_security': online_security,
        'online_backup': online_backup,
        'device_protection': device_protection,
        'tech_support': tech_support
}
    data_inf = pd.DataFrame([data_inf])
    # pca = clustering_pipeline.transfrom(data_inf)

    pred_process = st.button("Predict", use_container_width=True, type='primary')

        # The prediction process
    if pred_process:
        # Predict Inference set
        y_result = clustering_pipeline.predict(data_inf)

        if y_result == 0:
            # Cluster 0: "Premium"
            st.markdown("## Cluster 0: pengguna dengan biaya bulanan tinggi")
            st.markdown("Cluster 0 kelas ini berisi pengguna-pengguna yang biaya perbulanya termasuk rata-rata tinggi")   

        elif y_result == 1:
            # Cluster 1: "Economical"
            st.markdown("## Cluster 1: pengguna dengan biaya bulanan rendah")
            st.markdown("Cluster 1 kelas ini berisi pengguna-pengguna yang memilih produk-produk yang tidak berbiaya tinggi")

        elif y_result == 2:
            # Cluster 2: "Medium"
            st.markdown("## Cluster 2: pengguna lama")
            st.markdown("Cluster 2 kelas ini diisi oleh mayoritas pengguna lama dari produk ini, rata-rata dari mereka telah menggunakan selama lebih dari 50 bulan. Selain itu user pada cluster ini sebagian besar juga menerapkan layanan tambahan")
            # Create a table feature

        else:
            # Cluster 3: "Basic"
            st.markdown("## Cluster 3: pengguna baru dan tidak menggunakan tiket")
            st.markdown("Cluster 3 kelas ini diisi dari user-use baru yang mayoritas belm lama dalam menggunakan produk ini. Mayoritas dari mereka juga tidak menggunakan tiket teknologi untuk dicsount pada produk mereka. Selain itu user yang masuk custer ini merupakan user yang.")
     
# Run the app
if __name__ == '__main__':
    run()
