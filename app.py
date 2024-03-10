import streamlit as st
from page1 import main as page1_main
from page2 import main as page2_main
from page3 import main as page3_main

st.set_page_config(
    page_title="Health-Guard",
    page_icon= "heart"
)

st.sidebar.title("Health-Guard")
selected_page = st.sidebar.radio("Go to", ("Introduction","Page for Doctors", "Page for Users"))

if selected_page == "Introduction":
    page1_main()
elif selected_page == "Page for Doctors":
    page2_main()
elif selected_page == "Page for Users":
    page3_main()
