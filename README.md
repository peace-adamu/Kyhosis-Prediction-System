# Project Title: Kyphosis Detection System
[Project Overview](#project-overview)
[Features](#features)
[User input](#use-input)
[Prediction output](#prediction-output)
[Requirements](#requirements)
[Usage](#usage)
[Model](#model)
[Classification report](#classification-report)




## Project Overview
This project implements a web-based Kyphosis Detection System using Streamlit and a pre-trained Random Forest Classifier model. The system allows users to input patient data and predict the presence of kyphosis.

## Features
- Web-based interface built with Streamlit
- Predicts kyphosis presence using a pre-trained Random Forest Classifier model
- Model loaded from a joblib file
  
## User input: 
Kyphosis dataset contains features such as:
- Age: Age describes the age of the patient in months
- Number: describes the number of vertebrae involved in the curvature.
- Start:  describes the starting vertebra of the curvature.
  

#### Prediction output:
Kyphosis: is present (1) "You have kyphosis", or not (0) that is 0 = absent "You do not have kyphosis"

## Requirements
- Python 3.x
- Streamlit
- Scikit-learn
- Joblib
- Power BI

## Usage
- Install required packages: pip install streamlit scikit-learn joblib
- Run the app: streamlit run app.py
- Input patient data and click the "predict" button to get the prediction result

## Model
The pre-trained Random Forest Classifier model is loaded from a joblib file (rfc_model.joblib). The model is trained on a csv dataset and predicts kyphosis presence based on the input features.

## Classification report

```
precision    recall  f1-score   support

           0       1.00      1.00      1.00        11
           1       1.00      1.00      1.00         6

    accuracy                           1.00        17
   macro avg       1.00      1.00      1.00        17
weighted avg       1.00      1.00      1.00        17
```
## Confusion matrix
```
 [[11  0]
 [ 0  6]]
```
## Visualization
![g8](https://github.com/user-attachments/assets/9efb1a08-15a6-4973-9e2b-437d95520379)

![g9](https://github.com/user-attachments/assets/6213ee33-97e8-4736-9f58-6fbe5fbfac0f)
Heat map visual

![g10](https://github.com/user-attachments/assets/c8a77ff0-3e29-4f11-b28c-b4f830a237ad)
Pair plot visual

## Code
Python script code used to build the app
```
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import joblib

## Load the model
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
```
 

