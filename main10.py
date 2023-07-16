import streamlit as st
import pandas as pd

st.title("More Interactive Widgets")

slider = st.slider("This is a slider", min_value=0, max_value=100, value=50)
print(slider)

text_inp = st.text_input("Enter your course title", max_chars=20)

text_area = st.text_area("Enter your course description", max_chars=100)

date_inp = st.date_input("Enter your date registrator")

time_input = st.time_input("Enter your time")

print(time_input)
