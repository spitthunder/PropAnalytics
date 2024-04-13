import streamlit as st

# Define the sidebar options with 'Recommend' added
sidebar_options = ['Home', 'Price Predictor', 'Analytics App', 'Recommend']

# Render the sidebar
selected_option = st.sidebar.selectbox('Select an option', sidebar_options)

# Load modules based on selected option
if selected_option == 'Home':
    import home_module
    home_module.show_home_page()
elif selected_option == 'Price Predictor':
    import Price_predictor
    Price_predictor.show_price_predictor()
elif selected_option == 'Analytics App':
    import Analytics_App
    Analytics_App.show_analytics_app()
elif selected_option == 'Recommend':
    import recommender_system
    recommender_system.show_recommendation()
