import streamlit as st
import pickle
import pandas as pd


def show_recommendation():

    # Load data
    location_df = pickle.load(open('dataset/location_distance.pkl', 'rb'))
    cosine_sim1 = pickle.load(open('dataset/cosine_sim1.pkl', 'rb'))
    cosine_sim2 = pickle.load(open('dataset/cosine_sim2.pkl', 'rb'))
    cosine_sim3 = pickle.load(open('dataset/cosine_sim3.pkl', 'rb'))

    def recommend_properties_with_scores(property_name, top_n=5):
        # Compute weighted sum of cosine similarity matrices
        cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3

        # Get similarity scores for the property
        sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

        # Sort properties based on similarity scores
        sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get indices and scores of top_n most similar properties
        top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
        top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

        # Retrieve names of top properties
        top_properties = location_df.index[top_indices].tolist()

        # Create dataframe with results
        recommendations_df = pd.DataFrame({
            'PropertyName': top_properties,
            'SimilarityScore': top_scores
        })

        return recommendations_df

    st.title("Select Location and Radius")

    selected_location = st.selectbox('Location', sorted(location_df.columns.to_list()))
    radius = st.number_input('Radius in Kms')

    if st.button('Search'):
        result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()

        for key, value in result_ser.items():
            st.text(str(key) + " " + str(round(value / 1000)) + 'kms')

    st.title("Recommend Apartments")
    selected_apartment = st.selectbox('Select an apartment', sorted(location_df.index.to_list()))

    if st.button("Recommend"):
        recommendation_df = recommend_properties_with_scores(selected_apartment)
        st.dataframe(recommendation_df)



