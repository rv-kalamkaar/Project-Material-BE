import streamlit as st
from streamlit_option_menu import option_menu
import pickle as pkl

# importing pickle files

diabetes_model = pkl.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pkl.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pkl.load(open('parkinsons_model.sav', 'rb'))


# sidebar for nav

with st.sidebar:

    selected = option_menu("Health-Guard: Machine learning driven – disease prediction and personalized recommendation system",
                           ['Diabetes Prediction System',
                            'Heart Disease Prediction System',
                            'Parkinsons Disease Prediction System'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# diabetes prediction rate

if (selected == "Diabetes Prediction System"):

    # page title
    st.title('Diabetes Prediction System')
    # getting input data from the user
    # Columns for input fields

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('No of pregnancies', step=1)

    with col2:
        Glucose = st.number_input('Glucose Level',step=5)

    with col3:
        BloodPressure = st.number_input('Blood Pressure value',step=5)

    with col1:
        Skinthickness = st.number_input('Skin Thickness value',step=5)

    with col2:
        Insulin = st.number_input('Insulin Level',step=1)

    with col3:
        bmi_index = st.number_input('BMI value',step=5)

    with col1:
        DiabetesPedigreeFunction = st.number_input(
            "Diabetes Pedigree Function value",step=0.1)

    with col2:
        Age = st.number_input("Age of a person",step=1)

    # code for prediction
    diab_diagnosis = ' '

    # creating a button for prediction

    if st.button('Diabetes Test Result'):
        inputFeatures = [Pregnancies,Glucose,BloodPressure,Skinthickness,Insulin,bmi_index, DiabetesPedigreeFunction, Age]
        diab_prediction = diabetes_model.predict([inputFeatures])

        if (diab_prediction[0] == 1):
            diab_diagnosis = "The person is Diabetic"
        else:
            diab_diagnosis = "The person is not Diabetic"

    st.success(diab_diagnosis)

# Heart Disease Prediction Rate
if (selected == "Heart Disease Prediction System"):

    # page title
    st.title('Heart Disease Prediction System')

# Parkinsons Disease Prediction Rate
if (selected == "Parkinsons Disease Prediction System"):

    # page title
    st.title('Parkinsons Disease Prediction System')
