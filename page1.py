import streamlit as st
from streamlit_option_menu import option_menu
import pickle as pkl


def main():
    st.title("WELCOME TO HEALTH GAURD: ML based Disease Prediction system !! ")

    st.write("Health Guard is a machine learning-based system designed for multiple disease prediction and recommendation.")

    st.write("With Health Guard, you can:")
    st.write("- Predict the likelihood of various diseases based on input symptoms.")
    st.write("- Receive personalized recommendations for maintaining or improving your health.")

    st.write("Health Guard utilizes advanced machine learning algorithms to analyze symptoms and provide accurate predictions.")

    st.write("Get started by uploading your symptoms or exploring the features!")

    # Display the image with reduced size
    st.image("Intro Image.jpg", caption='Health Guard Logo', width=600)

if __name__ == "__main__":
    main()
