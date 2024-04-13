import streamlit as st
import pickle
import pandas as pd
import numpy as np

def show_price_predictor():    
    # Load DataFrame and pipeline from pickle files
    with open('dataset/df.pkl', 'rb') as file:
        df = pickle.load(file)
    
    with open('dataset/pipeline.pkl', 'rb') as file:
        pipeline = pickle.load(file)

    st.header('Enter your inputs')

    # Check if df is not empty
    if not df.empty:
        # Input widgets
        property_type = st.selectbox('Property Type', ['Flat', 'House'])
        sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))
        bedRoom = float(st.selectbox('Number of Bedrooms', sorted(df['bedRoom'].unique().tolist())))
        bathroom = float(st.selectbox('Number of Bathrooms', sorted(df['bathroom'].unique().tolist())))
        balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))
        property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))
        built_up_area = float(st.number_input('Built Up Area'))
        servant_room = float(st.selectbox('Servant Room', [0.0, 1.0]))
        store_room = float(st.selectbox('Store Room', [0.0, 1.0]))
        furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
        luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))
        floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))

        if st.button('Predict'):
            # Form a dataframe
            data = [[property_type, sector, bedRoom, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
            columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
                       'agePossession', 'built_up_area', 'servant room', 'store room',
                       'furnishing_type', 'luxury_category', 'floor_category']

            # Convert to DataFrame
            one_df = pd.DataFrame(data, columns=columns)

            st.dataframe(one_df)

            # Check if pipeline is not None
            if pipeline is not None:
                # Predict
                predicted_prices = pipeline.predict(one_df)
                if len(predicted_prices) > 0:
                    base_price = np.expm1(predicted_prices[0])
                    low = base_price - 0.22
                    high = base_price + 0.22
                    st.text("The Price of the flat is between {} Cr and {} Cr".format(round(low, 2), round(high, 2)))
                else:
                    st.warning("No prediction was made.")
            else:
                st.warning("Pipeline is not loaded correctly.")
    else:
        st.error("DataFrame 'df' is empty.")

