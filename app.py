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
                            icons =['activity','heart','person'],
                            default_index=0)
    

#*****************************************DIABETES SECTION********************************************

if (selected=="Diabetes Prediction System"):

    #page title
    st.title('Diabetes Prediction System')

    #getting input data from the user
    #Columns for input fields

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('No of pregnancies')

    with col2:
        Glucose = st.number_input('Glucose Level')

    with col3:
        BloodPressure = st.number_input('Blood Pressure value')

    with col1:
        Skinthickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        bmi_index = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")

    with col2:
        Age = st.text_input("Age of a person")




    #code for prediction
    diab_diagnosis = ' '

    #creating a button for prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([['Pregnancies','Glucose','BloodPressure','Skinthickness','Insulin','BMI','DiabetesPedigreeFunction','Age']])

        if (diab_prediction[0]==1):
            diab_diagnosis = "The person is Diabetic"
        else:
            diab_diagnosis = "The person is not Diabetic"

    st.success(diab_diagnosis)



#*****************************************HEART SECTION********************************************


# Heart Disease Prediction Rate
if (selected=="Heart Disease Prediction System"):

    #page title
    st.title('Heart Disease Prediction System')

    #getting input data from the user
    #Columns for input fields

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age of person')

    with col2:
        sex = st.text_input('Sex of person [Male = 1 / Female = 0 ] ')

    with col3:
        cp = st.text_input('Chest Pain type')

    with col1:
        trestbps = st.text_input('Resting blood pressure')

    with col2:
        chol = st.text_input('Cholestrol in mg/dl')

    with col3:
        fbs = st.text_input('Fasting blood pressure')

    with col1:
         restecg = st.text_input("Resting electrographic result")

    with col2:
        talach = st.text_input("Maximum heart rate achieved")

    with col3:
        exang = st.text_input("Exercise induced angina")

    with col1:
        oldpeak = st.text_input("ST depression induced by exercise relative to rest")

    with col2:
        slope = st.text_input("Slope of the peak exercise ST segment")

    with col3:
        ca = st.text_input("Number of major vessels (0-3) colored by flourosopy")

    with col1:
        thal = st.text_input("Thal: 0 = normal; 1 = fixed defect; 2 = reversable defect")



    #code for prediction
    heart_diagnosis = ' '

    #creating a button for prediction

    if st.button('Diabetes Test Result'):
        heart_prediction = heart_disease_model.predict([['Pregnancies','Glucose','BloodPressure','Skinthickness','Insulin','BMI','DiabetesPedigreeFunction','Age']])

        if (diab_prediction[0]==1):
            heart_diagnosis = "The person is Diabetic"
        else:
            heart_diagnosis = "The person is not Diabetic"

    st.success(heart_diagnosis)


    #*****************************************PARKISON SECTION********************************************

# Parkinsons Disease Prediction Rate
if (selected=="Parkinsons Disease Prediction System"):

    #page title
    st.title('Parkinsons Disease Prediction System')

    #getting input data from the user
    #Columns for input fields

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('No of pregnancies')

    with col2:
        Glucose = st.number_input('Glucose Level')

    with col3:
        BloodPressure = st.number_input('Blood Pressure value')

    with col1:
        Skinthickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        bmi_index = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")

    with col2:
        Age = st.text_input("Age of a person")




    #code for prediction
    diab_diagnosis = ' '

    #creating a button for prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([['Pregnancies','Glucose','BloodPressure','Skinthickness','Insulin','BMI','DiabetesPedigreeFunction','Age']])

        if (diab_prediction[0]==1):
            diab_diagnosis = "The person is Diabetic"
        else:
            diab_diagnosis = "The person is not Diabetic"

    st.success(diab_diagnosis)
