import streamlit as st
import pandas as pd
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np

x=np.linspace(0, 10, 100)

bar_x=np.array([1,2,3,4,5])

st.markdown("<h1 style='text-align: center; color: red;'>User Registration</h1>", unsafe_allow_html=True)

st.sidebar.write("This is our sidebar")

opts = st.sidebar.radio("choose your chart", options=("Bar","H-Bar","Line"))

if opts == "Line":
    fig = plt.figure()
    plt.plot(x, np.sin(x))
    st.write(fig)
elif opts == "Bar":
    fig = plt.figure()
    plt.bar(bar_x*10, bar_x)
    st.write(fig)
else:
    fig = plt.figure()
    plt.barh(bar_x*10, bar_x)
    st.write(fig)


