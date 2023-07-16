import streamlit as st
import pandas as pd
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np

text = "DOG"

if "click" not in st.session_state:
    st.session_state.click=False
else:
    if st.session_state.click==False:
        text = "CAT"
        st.session_state.click=True
    else:
        text = "DOG"
        st.session_state.click=False

st.button(text)