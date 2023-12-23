import streamlit as st
import pickle as pkl
from sklearn.preprocessing import LabelEncoder
import numpy as np

def main():
    st.title("Multiple diseases prediction for users")
    with open('multiple_disease.sav', 'rb') as file:
        loaded_model = pkl.load(file)

    model = loaded_model['model']
    label_encoder = loaded_model['label_encoder']
    
    
    # getting input data from the user
    # Columns for input fields

    col1, col2, col3 = st.columns(3)
    
    display_yes_no = ("No", "Yes")
    
    options_yes_no = list(range(len(display_yes_no)))
    
    print(options_yes_no)

    with col1:
        itching = st.selectbox('Does the user/patient have itching problem ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x], key=1)

    with col2:
            skin_rash = st.selectbox('Does the user/patient have skin rash ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x], key=2)

    with col3:
            continuous_sneezing = st.selectbox('Does the user/patient have continuous sneezing problem ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=3)

    with col1:
            shivering = st.selectbox('Does the user/patient have shivering in body ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=4)

    with col2:
            joint_pain = st.selectbox('Does the user/patient have joint pain ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=5)

    with col3:
            stomach_pain = st.selectbox('Does the user/patient have stomach pain ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=6)

    with col1:
            acidity = st.selectbox('Does the user/patient have acidity ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=7)

    with col2:
            vomiting = st.selectbox('Does the user/patient performed vomiting ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=8)

    with col3:
            fatigue = st.selectbox('Does the user/patient had fatigue ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=9)

    with col1:
            weight_gain = st.selectbox('Does the user/patient have gained weight ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=10)
    
    with col2:
            anxiety = st.selectbox('Does the user/patient have anxiety problem ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=11)

    with col3:
            mood_swings = st.selectbox('Does the user/patient have mood swings problem ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=12)

    with col1:
            weight_loss = st.selectbox('Does the user/patient have lost weight ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=13)
    
    with col2:
            restlessness = st.selectbox('Does the user/patient have restlessness ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=14)

    with col3:
            irregular_sugar_level = st.selectbox('Does the user/patient have irregular sugar level problem? ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=15)

    with col1:
            cough = st.selectbox('Does the user/patient have cough ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=16)
    
    with col2:
            high_fever = st.selectbox('Does the user/patient have high fever ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=17)

    with col3:
            breathlessness = st.selectbox('Does the user/patient have breathlessness ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=18)

    with col1:
            sweating = st.selectbox('Does the user/patient have sweating problem ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=19)
    
    with col2:
            dehydration = st.selectbox('Does the user/patient have dehydration ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=20)

    with col3:
            indigestion = st.selectbox('Does the user/patient have indigestion problem ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=21)

    with col1:
            headache = st.selectbox('Does the user/patient have headache problem ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=22)
    
    with col2:
            nausea = st.selectbox('Does the user/patient have suffered from nausea ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=23)

    with col3:
            loss_of_appetite = st.selectbox('Does the user/patient have a loss of appetite ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=24)

    with col1:
            back_pain = st.selectbox('Does the user/patient have back pain ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=25)
    
    with col2:
            constipation = st.selectbox('Does the user/patient have constipation ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=26)

    with col3:
            abdominal_pain = st.selectbox('Does the user/patient have abdominal pain ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=27)   
    
    with col1:
            diarrhoea = st.selectbox('Does the user/patient have diarrhoea ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=28)
    
    with col2:
            mild_fever = st.selectbox('Does the user/patient have mild fever ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=29)

    with col3:
            yellow_urine = st.selectbox('Does the user/patient have yellow urine ?',
                           options_yes_no, format_func=lambda x: display_yes_no[x],key=30)
                
    # # code for prediction
    user_diagnosis = ' '

    # creating a button for prediction

    if st.button('Test Results'):
            inputFeatures = [itching,skin_rash,continuous_sneezing,shivering,joint_pain,stomach_pain,acidity,vomiting,fatigue,weight_gain,anxiety,mood_swings,weight_loss,restlessness,irregular_sugar_level,cough,high_fever,breathlessness,sweating,dehydration,indigestion,headache,nausea,loss_of_appetite,back_pain,constipation,abdominal_pain,diarrhoea,mild_fever,yellow_urine]
            
            input_data_as_numpy_array = np.asarray(inputFeatures)
            input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
            
            new_data_predictions = model.predict(input_data_reshaped)
            new_data_predictions_decoded = label_encoder.inverse_transform(new_data_predictions)
            
            output = str(new_data_predictions_decoded).strip("['']")
            
            
            
            user_diagnosis = f"The person is having {output}"

    st.success(user_diagnosis)


if __name__ == "__main__":
    main()