import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the model
model = joblib.load('rfc_model.joblib')

# Title of the app
st.title("Kyphosis Detection System")

# App Description
st.markdown(
    """
    ## About This App 
      Kyphosis is a spinal disorder characterized by an excessive outward curvature of the upper back (thoracic spine), leading to a rounded or hunched posture. It can occur due to various reasons.
    ##### This is a **Kyphosis Prediction Web App** that uses machine learning to predict the presence of kyphosis in patients.  
    - **Age**: The age of the patient (in months).  
    - **Number**: The number of vertebrae involved in the curvature.  
    - **Start**: The starting vertebra of the curvature.  
    """
)

# Initialize session state
if 'prediction' not in st.session_state:
    st.session_state.prediction = None

# Function to get user input
def get_user_input():
    age = st.number_input("Age", value=None, placeholder="Enter the age in months", min_value=0, max_value=200, key="age_input")
    number = st.number_input("Number", value=None, placeholder="Enter the number of vertebrae involved in the curvature", min_value=0, max_value=10, key="number_input")
    start = st.number_input("Start", value=None, placeholder="Enter the starting vertebra of the curvature", min_value=0, max_value=18, key="start_input")
    return age, number, start

# Function to make prediction
def make_prediction(age, number, start):
    result = model.predict([[age, number, start]])
    return result[0]  # Return a single value instead of an array

# Main app
age, number, start = get_user_input()

if st.button("Predict Kyphosis"):
    if age is None or number is None or start is None:
        st.error("Please enter all values before making a prediction.")
    else:
        st.session_state.prediction = make_prediction(age, number, start)

# Show result if prediction exists
if st.session_state.prediction is not None:
    st.subheader("Prediction Result:")
    if st.session_state.prediction == 0:
        st.success("You do not have kyphosis.")
    else:
        st.warning("Kyphosis is present.")

    # Ask if user wants to make another prediction
    if st.button("Make Another Prediction"):
        st.session_state.prediction = None  # Reset the prediction
        st.rerun()  # Refresh the app
