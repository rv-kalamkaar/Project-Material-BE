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
        bmi_index = st.number_input('BMI value', step = 5)

    with col1:
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function value", step = 0.1)

    with col2:
        Age = st.number_input("Age of a person",step = 1)




    #code for prediction
    diab_diagnosis = ' '

    #creating a button for prediction

    if st.button('Diabetes Test Result'):
        inputFeatures = [Pregnancies , Glucose, BloodPressure, Skinthickness ,Insulin , bmi_index ,DiabetesPedigreeFunction, Age]
        diab_prediction = diabetes_model.predict([inputFeatures])

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
        age = st.number_input('Age', step=1)

    with col2:
        options1 = {
            'Female' : 0,
            'Male': 1
        }
        sex = st.selectbox("Gender",options=list(options1.values()))

    with col3:
        options2 = {
            'Angina' : 1,
            'Asymptomatic' : 2,
            'Abnormal' : 3,
            'Severe' : 4
        }
        cp = st.selectbox('Chest Pain type/condition',options= list(options2.values()))

    with col1:
        trestbps = st.number_input('Resting blood pressure',step = 10)

    with col2:
        chol = st.number_input('Cholestrol in mg/dl', step = 10)

    with col3:

        options3 = {
            'Yes' : 1,
            'No' : 0
        }
        fbs = st.selectbox('Fasting blood pressure > 120 Mg/dl', options=list(options3.values()))

    with col1:

        options4 = {
            'Normal' : 0,
            'Abnormal': 1,
            'Hyper':2
        }
        restecg = st.selectbox("Resting electrographic result",options=list(options4.values()))

    with col2:
        thalach = st.number_input("Maximum heart rate achieved",step=5)

    with col3:
        options5 = {
            'Yes' : 1,
            'No' : 0
        }
        exang = st.selectbox("Exercise induced angina",options=list(options5.values()))

    with col1:
        oldpeak = st.number_input("ST depression induced by exercise relative to rest", min_value = 0.0, step=0.1)

    with col2:

        options6 = {
            'Up' : 1,
            'Flat': 2,
            'Down':3
        }
        slope = st.selectbox("Slope of the peak exercise ST segment",options=list(options6.values()))

    with col3:

        options7 = {
            'None' : 0,
            'One' : 1,
            'Two' : 2,
            'Three' : 3
        }
        ca = st.selectbox("Number of major vessels (0-3) colored by flourosopy", options=list(options7.values()))

    with col1:

        options8 = {
            'Normal' : 0,
            'Fixed Defect': 1,
            'Reversable Defect':2
        }
        thal = st.selectbox("Thal",options=list(options8.values()))



    #code for prediction
    heart_diagnosis = ' '

    #creating a button for prediction

    if st.button('Heart Test Result'):
        inputFeatures2 = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        print(inputFeatures2)
        heart_prediction = heart_disease_model.predict([inputFeatures2])

        if (heart_prediction[0]==1):
            heart_diagnosis = "The person is affected by heart disease"
        else:
            heart_diagnosis = "The person is not affected by heart disease"

    st.success(heart_diagnosis)


    #*****************************************PARKISON SECTION********************************************


# Parkinsons Prediction Page  
if (selected == 'Parkinsons Disease Prediction System'):    
    
    # page title
    st.title("Parkinsons Disease Prediction System")

    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP: Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP: Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP: Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP: Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP: RAP')
        
    with col2:
        PPQ = st.text_input('MDVP: PPQ')
        
    with col3:
        DDP = st.text_input('Jitter: DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP: Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP: Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer: APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer: APQ5')
        
    with col3:
        APQ = st.text_input('MDVP: APQ')
        
    with col4:
        DDA = st.text_input('Shimmer: DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        if not all([fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]):
            st.warning("Please fill in all the fields.")
        else:
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
            
            if (parkinsons_prediction[0] == 1):
              parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
              parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)    

    