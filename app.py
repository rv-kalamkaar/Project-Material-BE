import streamlit as st
from streamlit_option_menu import option_menu
import pickle as pkl

# importing pickle files

diabetes_model = pkl.load(open("D:\Rohan Vikramaditya\Project Material BE\diabetes_model.sav"))

heart_disease_model = pkl.load(open("D:\Rohan Vikramaditya\Project Material BE\heart_disease_model.sav"))

parkinsons_model = pkl.load(open("D:\Rohan Vikramaditya\Project Material BE\parkinsons_model.sav"))