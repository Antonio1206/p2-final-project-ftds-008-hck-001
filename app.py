import streamlit as st
import eda
import prediction
import model

page = st.sidebar.selectbox(label='Select Page:', options=['📒 Home Page', ' 📊 Exploration Data Analysis', '💻 cluster predict','💻 churn predict'])

if page == '📒 Home Page':
    st.image("logo2.jpg", width=20, caption='Logo', use_column_width=True)
    st.subheader('🔗[Yobi Aditias](https://www.linkedin.com/in/yobi-aditias-109781235/)')
    st.subheader('🔗[Muhammad Rofi Senoaji](link_muhammad_rofi)')
    st.subheader('🔗[Antonius Dwiputra Daeng](https://www.linkedin.com/in/antonius-daeng-331793289/)')
    st.header('Description')
    st.markdown('''
                "Churn Tracker" is a telecom customer churn analysis app that utilizes advanced analytics and predictive models for real-time monitoring, 
                segmentation, and targeted marketing. It helps providers reduce churn, boost customer satisfaction, and optimize resources for enhanced profitability, 
                making it an essential tool for the competitive telecom industry.
                ''')
    st.header('Project Objective')
    st.markdown('''
                The objectives of this research are to achieve success by addressing the key challenges in the telecommunications industry, which include reducing churn rate, 
                understanding the factors influencing customer churn, uncovering customer behavior patterns related to churn, and designing innovative customer 
                retention strategies to drive company profitability growth in a short time frame.
                ''')

elif page == ' 📊 Exploration Data Analysis':
    eda.run()

elif page == '💻 cluster predict':
    prediction.run()

elif page == '💻 churn predict':
    model.run()


