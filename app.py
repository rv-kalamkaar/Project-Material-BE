import streamlit as st
from page1 import main as page1_main
from page2 import main as page2_main
from streamlit_option_menu import option_menu
import pickle as pkl

st.set_page_config(
    page_title="Health-Guard",
    page_icon= "heart"
)

st.sidebar.title("Health-Guard: Machine learning driven – disease prediction and personalized recommendation system")
selected_page = st.sidebar.radio("Go to", ("Page for Doctors", "Page for Users"))

if selected_page == "Page for Doctors":
    page1_main()
elif selected_page == "Page for Users":
    page2_main()
# importing pickle files
