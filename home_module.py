import streamlit as st

def show_home_page():

    # Set the title of the page
    st.title("Welcome to PropAnalytics")

    # Introduction section
    st.header("Introduction")
    st.write("""
    PropAnalytics is a cutting-edge real estate analysis platform designed to 
    leverage machine learning and data visualization to provide deep insights 
    into the real estate market of Gurgaon. Our tools help users evaluate property 
    values, understand market trends, and receive personalized property recommendations.
    """)

    # About the project
    st.header("About the Project")
    st.write("""
    The project combines various technologies including Python, Pandas, Seaborn, and 
    Streamlit to create an interactive web application that is both informative and 
    easy to use. Users can predict property prices, visualize market data, and explore
    potential investment opportunities with just a few clicks.
    """)

    # Navigation instructions
    st.header("Getting Started")
    st.write("""
    To begin exploring the features of PropAnalytics, use the navigation options on 
    the left sidebar:
    - **Price Predictor**: Estimate the price of properties based on various factors.
    - **Analytics Module**: Dive into visual data analysis of the real estate market.
    - **Recommendation Engine**: Get personalized property recommendations.
    """)

    # Footer
    st.header("Start Your Analysis")
    st.write("""
    Select an option from the sidebar to start exploring data-driven insights into 
    the real estate market. Whether you are a home buyer, seller, or real estate enthusiast, 
    PropAnalytics provides valuable tools to assist you in making informed decisions.
    """)