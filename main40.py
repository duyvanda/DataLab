import streamlit as st
import pandas as pd
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np

x=np.linspace(0, 10, 100)

bar_x=np.array([1,2,3,4,5])

st.markdown("<h1 style='text-align: center; color: red;'>Callbacks</h1>", unsafe_allow_html=True)

def printer(name):
    print("Message")

input = st.text_input("Enter your name")
sbtn = st.button("Submit")
if sbtn:
    st.checkbox("Want to display your name?", on_change=printer, args=(input, ))

