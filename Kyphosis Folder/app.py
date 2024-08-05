import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the model
model = joblib.load('rfc_model.joblib')

# Title of the app
st.title("Kyphosis Detection System")

# Initialize session state
if 'prediction' not in st.session_state:
    st.session_state.prediction = None

# Function to get user input
def get_user_input():
    age = st.number_input("Age", value=None, placeholder="Enter the age in months", min_value=0, max_value=200, key="age")
    number = st.number_input("Number", value=None, placeholder="Enter the number of vertebrae involved in the curvature", min_value=0, max_value=10, key="number")
    start = st.number_input("Start", value=None, placeholder="Enter the starting vertebra of the curvature", min_value=0, max_value=18, key="start")
    return age, number, start

# Function to make prediction
def make_prediction(age, number, start):
    result = model.predict([[age, number, start]])
    return result

# Main app
while True:
    if st.session_state.prediction is None:
        age, number, start = get_user_input()
        if st.button("Predict Kyphosis"):
            result = make_prediction(age, number, start)
            st.session_state.prediction = result
    else:
        if st.session_state.prediction == 0:
            st.write("You do not have kyphosis")
        else:
            st.write("Kyphosis is present")

        another_prediction = st.selectbox("Do you want to make another prediction?", ["Yes", "No"], key="another_prediction")
        if another_prediction == "No":
            st.write("Thank you for using Kyphosis Detection System! Check back later.")
            break
        else:
            st.session_state.prediction = None