import streamlit as st
import pandas as pd

st.title("uploading file")

images = st.file_uploader("multi", type=['png','jpg'], accept_multiple_files=True)

for i in images:
    st.image(i)