import streamlit as st
import pandas as pd
import time as ts
from datetime import time

st.title("Timer App With Progress Bar")

bar = st.progress(0)

for i in range(10):
    bar.progress(i*10)
    time.sleep(0.3)

def converter(value):
    m,s,mm = value.split(":")
    


