import streamlit as st
import pandas as pd
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np

@st.cache_data()
def printer():
    st.write("Running")
    ts.sleep(3)
    return "Message"

st.write(printer())