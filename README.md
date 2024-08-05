Kyphosis Detection System
Overview
This project implements a web-based Kyphosis Detection System using Streamlit and a pre-trained Random Forest Classifier model. The system allows users to input patient data and predict the presence of kyphosis.
Features
Web-based interface built with Streamlit
Predicts kyphosis presence using a pre-trained Random Forest Classifier model
Model loaded from a joblib file
User input:
Age
Number
Start
Prediction output:
"You do not have kyphosis" or "Kyphosis is present"
Requirements
Python 3.x
Streamlit
Scikit-learn
Joblib
Usage
Install required packages: pip install streamlit scikit-learn joblib
Run the app: streamlit run app.py
Input patient data and click the "predict" button to get the prediction result
Model
The pre-trained Random Forest Classifier model is loaded from a joblib file (rfc_model.joblib). The model is trained on a dataset and predicts kyphosis presence based on the input features.



