import streamlit as st
from page1 import main as page1_main
from page2 import main as page2_main
from page3 import main as page3_main

st.set_page_config(
    page_title="Health-Guard ",
    page_icon= "heart"
)

st.sidebar.title("Health-Guard {Precaution is always better than cure!!} \n WARNING !! ----> If Normal users ----> Go to 'Page for Users !!  Avoid going to Doctor's Page' ")
selected_page = st.sidebar.radio("Go to", ("Introduction","Page for Doctors \n (For medical Staff only)", "Page for Users"))

if selected_page == "Introduction":
    page1_main()
elif selected_page == "Page for Doctors \n (For medical Staff only)":
    page2_main()
elif selected_page == "Page for Users":
    page3_main()
