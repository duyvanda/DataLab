import streamlit as st
import pandas as pd
import time as ts
from datetime import time

st.markdown("<h1 style='text-align: center; color: red;'>User Registration</h1>", unsafe_allow_html=True)

with st.form("form-2"):
    col1, col2 = st.columns(2)
    f_n = col1.text_input("First Name")
    l_n = col2.text_input("Last Name")
    st.text_input("Email")
    st.text_input("Pass")
    st.text_input("Confirm Pass")
    s_state = st.form_submit_button("Submit")

    if s_state:
        if f_n == '':
            st.warning("Please fill above")
        else:
            st.success("Please fill above")