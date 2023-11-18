import streamlit as st
from page1 import main as page1_main
from page2 import main as page2_main
from page3 import main as page3_main
from streamlit_option_menu import option_menu
import pickle as pkl

st.set_page_config(
    page_title="Health-Guard",
    page_icon= "heart"
)

st.sidebar.title("Health-Guard: Machine learning driven – disease prediction and personalized recommendation system")
selected_page = st.sidebar.radio("Go to", ("Introduction","Page for Doctors", "Page for Users"))

if selected_page == "Introduction":
    page1_main()
elif selected_page == "Page for Doctors":
    page2_main()
elif selected_page == "Page for Users":
    page3_main()
# importing pickle files

diabetes_model = pkl.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pkl.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pkl.load(open('parkinsons_model.sav', 'rb'))

breast_model = pkl.load(open('breast_cancer_model.sav', 'rb'))

lung_model = pkl.load(open('lung_cancer_model.sav', 'rb'))

kidney_model = pkl.load(open('kidney.pkl', 'rb'))

liver_model = pkl.load(open('liver.pkl', 'rb'))



# sidebar for nav

with st.sidebar:

    selected = option_menu("Health-Guard: Machine learning driven – disease prediction and personalized recommendation system",
                           ['Diabetes Prediction System',
                            'Heart Disease Prediction System',
                            'Parkinsons Disease Prediction System',
                            'Breast Cancer Prediction System',
                            'Lung Cancer Prediction System',
                            'Kidney Disease Prediction System',
                            'Liver Disease Prediction System'],
                            icons =['activity','heart','person','gender-female','lungs','person-fill','person'],
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

        display_gen = ("Male", "Female")

        options_gen = list(range(len(display_gen)))

        sex = st.selectbox("Gender", options_gen, format_func=lambda x: display_gen[x])

    with col3:

        display2 = ("Angina", "Asymptomatic","Abnormal","Severe")
        options2 = list(range(len(display2)))
        cp = st.selectbox('Chest Pain type/condition', options2, format_func=lambda x: display2[x])

    with col1:
        trestbps = st.number_input('Resting blood pressure',step = 10)

    with col2:
        chol = st.number_input('Cholestrol in mg/dl', step = 10)

    with col3:


        display_yes_no = ("Yes", "No")

        options_yes_no = list(range(len(display_yes_no)))

        fbs = st.selectbox('Fasting blood pressure > 120 Mg/dl', options_yes_no, format_func=lambda x: display_yes_no[x])

    with col1:

        display4 = ('Normal','Abnormal', 'Hyper')

        options4 = list(range(len(display4)))

        restecg = st.selectbox("Resting electrographic result",options4, format_func=lambda x: display4[x])

    with col2:
        thalach = st.number_input("Maximum heart rate achieved",step=5)

    with col3:

        exang = st.selectbox("Exercise induced angina",options_yes_no, format_func=lambda x: display_yes_no[x])

    with col1:
        oldpeak = st.number_input("ST depression induced by exercise relative to rest", min_value = 0.0, step=0.1)

    with col2:

        display6 = ('Up','Flat','Down')

        options6 = list(range(len(display6)))

        slope = st.selectbox("Slope of the peak exercise ST segment",options6, format_func=lambda x: display6[x])

    with col3:

        display7 = ('None','One','Two','Three')

        options7 = list(range(len(display7)))

        ca = st.selectbox("Number of major vessels (0-3) colored by flourosopy",options7, format_func=lambda x: display7[x])

    with col1:

        display8 = ('Normal','Fixed Defect','Reversable Defect')

        options8 = list(range(len(display8)))

        thal = st.selectbox("Thal",options8, format_func=lambda x: display8[x])




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

    

#*****************************************BREAST CANCER SECTION********************************************

# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction System':
    # Page title
    st.title('Breast Cancer Prediction System')

    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        mean_radius = st.number_input('Mean Radius')

        mean_smoothness = st.number_input('Mean Smoothness')
        
        mean_symmetry = st.number_input('Mean Symmetry')

        perimeter_error = st.number_input('Perimeter Error')

    with col2:
        mean_texture = st.number_input('Mean Texture')

        mean_compactness = st.number_input('Mean Compactness')

        mean_fractal_dimension = st.number_input('Mean Fractal Dimension')
        
        area_error = st.number_input('Area Error')

    with col3:
        mean_perimeter = st.number_input('Mean Perimeter')

        mean_concavity = st.number_input('Mean Concavity')
        
        radius_error = st.number_input('Radius Error')    

        smoothness_error = st.number_input('Smoothness Error')

    with col4:
        mean_area = st.number_input('Mean Area')

        mean_concave_points = st.number_input('Mean Concave Points')
        
        texture_error = st.number_input('Texture Error')

        compactness_error = st.number_input('Compactness Error')


    with col1:
        concavity_error = st.number_input('Concavity Error')
        
        worst_radius = st.number_input('Worst Radius')
        
        worst_smoothness = st.number_input('Worst Smoothness')
        
        worst_symmetry = st.number_input('Worst Symmetry')

    with col2:        
        concave_points_error = st.number_input('Concave Points Error')
        
        worst_texture = st.number_input('Worst Texture')
        
        worst_compactness = st.number_input('Worst Compactness')
        
        worst_fractal_dimension = st.number_input('Worst Fractal Dimension')

    with col3:
        symmetry_error = st.number_input('Symmetry Error')
        
        worst_perimeter = st.number_input('Worst Perimeter')
        
        worst_concavity = st.number_input('Worst Concavity')

    with col4:
        fractal_dimension_error = st.number_input('Fractal Dimension Error')
        
        worst_area = st.number_input('Worst Area')
        
        worst_concave_points = st.number_input('Worst Concave Points')

        
    # Code for prediction
    cancer_diagnosis = ''
    
    # Creating a button for prediction
    if st.button('Breast Cancer Test Result'):
        if not all([mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness,
                    mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension, radius_error,
                    texture_error, perimeter_error, area_error, smoothness_error, compactness_error, concavity_error,
                    concave_points_error, symmetry_error, fractal_dimension_error, worst_radius, worst_texture,
                    worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concavity,
                    worst_concave_points, worst_symmetry, worst_fractal_dimension]):
            st.warning("Please fill in all the fields.")
        else:
            cancer_prediction = breast_model.predict([[mean_radius, mean_texture, mean_perimeter, mean_area,
                                                       mean_smoothness, mean_compactness, mean_concavity,
                                                       mean_concave_points, mean_symmetry, mean_fractal_dimension,
                                                       radius_error, texture_error, perimeter_error, area_error,
                                                       smoothness_error, compactness_error, concavity_error,
                                                       concave_points_error, symmetry_error, fractal_dimension_error,
                                                       worst_radius, worst_texture, worst_perimeter, worst_area,
                                                       worst_smoothness, worst_compactness, worst_concavity,
                                                       worst_concave_points, worst_symmetry, worst_fractal_dimension]])
            
            if cancer_prediction[0] == 1:
                cancer_diagnosis = 'The person is diagnosed with breast cancer.'
            else:
                cancer_diagnosis = 'The person is not diagnosed with breast cancer.'
        
    st.success(cancer_diagnosis)

#*****************************************DIABETES SECTION********************************************

if (selected=="Lung Cancer Prediction System"):

    #page title
    st.title('Lung Cancer Prediction System')

    #getting input data from the user
    #Columns for input fields

    col1, col2, col3, col4 = st.columns(4)

    
    display_gen = ("Male", "Female")

    options_gen = list(range(len(display_gen)))
    



    with col1:
        gender = st.selectbox("Gender", options_gen, format_func=lambda x: display_gen[x])

    with col2:
        age = st.number_input('Age',step=5)

    with col3:

        display_yes_no = ("Yes", "No")
        options_yes_no = list(range(len(display_yes_no)))

        smoking = st.selectbox("Do the person smoke?", options_yes_no, format_func=lambda x: display_yes_no[x])

    with col4:
        display_yes_no = ("Yes", "No")

        options_yes_no = list(range(len(display_yes_no)))
        yellow_fingers = st.selectbox("Does the person have yellow fingers?",options_yes_no,format_func=lambda x: display_yes_no[x])

    with col1:
        display_yes_no = ("Yes", "No")

        options_yes_no = list(range(len(display_yes_no)))
        anxiety = st.selectbox("Does the person have Anxiety issues?",options_yes_no,format_func=lambda x: display_yes_no[x])

    with col2:        
        display_yes_no = ("Yes", "No")

        options_yes_no = list(range(len(display_yes_no)))
        peer_pressure = st.selectbox("Does the person have Peer Pressure problems?",options_yes_no,format_func=lambda x: display_yes_no[x])

    with col3:
        display_yes_no = ("Yes", "No")

        options_yes_no = list(range(len(display_yes_no)))
        chr_disease = st.selectbox("Does the person have any chronic disease?",options_yes_no,format_func=lambda x: display_yes_no[x])

    with col4:
        display_yes_no = ("Yes", "No")

        options_yes_no = list(range(len(display_yes_no)))
        fatigue = st.selectbox("Does the person get fatigue easily?",options_yes_no,format_func=lambda x: display_yes_no[x])

    with col1:
        display_yes_no = ("Yes", "No")

        options_yes_no = list(range(len(display_yes_no)))


        allergy = st.selectbox("Does the person have any allergies?",options_yes_no,format_func=lambda x: display_yes_no[x])

    with col2:
        display_yes_no = ("Yes", "No")

        options_yes_no = list(range(len(display_yes_no)))
        wheezing = st.selectbox("Does the person have wheezing problem?",options_yes_no,format_func=lambda x: display_yes_no[x])

    with col3:
        display_yes_no = ("Yes", "No")

        options_yes_no = list(range(len(display_yes_no)))
        alcohol_consumption = st.selectbox("Does the person consume alcohol?",options_yes_no,format_func=lambda x: display_yes_no[x])

    with col4:
        display_yes_no = ("Yes", "No")

        options_yes_no = list(range(len(display_yes_no)))
        coughing = st.selectbox("Does the person have coughing?",options_yes_no,format_func=lambda x: display_yes_no[x])

    with col1:
        shortness_of_breath = st.selectbox("Does the person have shortness in breathing?",options_yes_no,format_func=lambda x: display_yes_no[x])

    with col2:
        swallowing_difficulty = st.selectbox("Does the person have yellow fingers?",options_yes_no,format_func=lambda x: display_yes_no[x])

    with col3:
        chest_pain = st.selectbox("Does the person have chest pain?",options_yes_no,format_func=lambda x: display_yes_no[x])




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
