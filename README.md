# PropAnalytics: A Machine Learning Odyssey in Real Estate Analysis

## Project Overview
PropAnalytics is an advanced real estate analysis platform developed to harness the power of machine learning to provide insights into property valuations and market dynamics within the Gurgaon region. Utilizing various data visualization and machine learning techniques, this project offers users a comprehensive tool to predict property prices, analyze market trends, and receive tailored property recommendations.

## Features
- **Price Predictor**: Leverages machine learning to provide property price estimations based on user-defined criteria.
- **Analytics Module**: Offers interactive visualizations such as geo-maps, word clouds, and statistical plots to analyze the real estate market.
- **Recommendation Engine**: Provides personalized property recommendations using content-based filtering.
  
All modules are integrated into a user-friendly web interface built with Streamlit, making complex data analyses accessible to all users.

## Technical Stack
- **Python**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization
- **Streamlit**: Web application framework
- **Scikit-learn**: Machine learning library, specifically version 1.4.1.post1 for the machine learning pipeline
- **Seaborn and Plotly**: Enhanced data visualization
- **WordCloud**: Visualization of key textual data
- **Pickle**: Object serialization
  
## How to Run the Web Application

### Prerequisites
- Python 3.8+
- Pip package manager

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/spitthunder/PropAnalytics.git
   cd PropAnalytics
   ```
2. Install the required Python Packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Navigate to the Project directory:
   ```bash
   cd path/to/your/project
   ```
2. In dataset folder, de-compress pipeline.rar. 
3. Run the Streamlit Web Application:
   ```bash
   streamlit run home.py
   ```
   
## Accessing the Web Application
Once the server is running, open a web browser and go to http://localhost:8501. This will load the PropAnalytics platform where you can interact with the various analytical tools provided.

## Contributions
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change. Ensure to update tests as appropriate.








