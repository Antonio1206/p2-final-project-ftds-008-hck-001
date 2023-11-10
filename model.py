import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

with open("finale.pkl", "rb") as file1:
    classification_pipeline = pickle.load(file1)

with open("finaleclustering.pkl", "rb") as file2:
    clustering_pipeline = pickle.load(file2)

def run():
    st.title('Churn Prediction')
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


    pred_process = st.button("Predict", use_container_width=True, type='primary')


    if pred_process:

        y_result = classification_pipeline.predict(data_inf)

        if y_result == 'Yes':

            st.markdown("## Custumer Churn")
            st.markdown("Customer Churn is the phenomenon where customers leave a product or service, reflecting dissatisfaction, changing needs, or the presence of more appealing alternatives.")   

        elif y_result == 'No':

            st.markdown("## Custumer Loyal")
            st.markdown("Loyal customers are those who consistently use a company's products or services over a longer period.")

     
# Run the app
if __name__ == '__main__':
    run()