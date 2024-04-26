import streamlit as st
from streamlit_option_menu import option_menu
import pickle as pkl


def main():

    st.title("Multiple Disease Prediction and Personalized Recommendation System using Machine Learning")
    st.write("Welcome to our project, where we have developed a system that predicts multiple diseases based on various symptoms and provides personalized recommendations for treatment and prevention.")
    st.write("Our system utilizes machine learning algorithms to analyze symptoms provided by users and predict possible diseases. Additionally, it offers personalized recommendations for treatment and preventive measures based on individual health data.")

    st.write("## How it works")
    st.write("1. **Symptom Input**: Users input their symptoms into the system.")
    st.write("2. **Machine Learning Prediction**: The system employs machine learning models to predict potential diseases based on the symptoms provided.")
    st.write("3. **Personalized Recommendations**: Based on the predicted diseases and user health data, personalized recommendations for treatment and prevention are provided.")

    st.write("## Why Use Our System?")
    st.write("- **Efficiency**: Quickly identify potential diseases based on symptoms.")
    st.write("- **Personalization**: Get personalized recommendations tailored to individual health data.")
    st.write("- **Preventive Measures**: Receive suggestions for preventive measures to maintain good health.")


    # Display project images
    st.image("Intro Image.jpg", caption='Health Guard', width=600)

if __name__ == "__main__":
    main()
