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
                            default_index=0)
    

# diabetes prediction rate

if (selected=="Diabetes Prediction System"):

    #page title
    st.title('Diabetes Prediction System')

if (selected=="Heart Disease Prediction System"):

    #page title
    st.title('Heart Disease Prediction System')

if (selected=="Parkinsons Disease Prediction System"):

    #page title
    st.title('Parkinsons Disease Prediction System')
