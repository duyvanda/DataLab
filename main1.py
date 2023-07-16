import streamlit as st
import pandas as pd

table = pd.DataFrame({"Col1":[1,2,3], "Col2":[4,5,6]})

st.metric(label="Sales", value="600M", delta="60%")

st.metric(label="Debt", value="700M", delta="-10%")

st.table(table)

st.dataframe(table)

# https://samplelib.com/sample-mp3.html

st.image("sample-boat-400x300.png", caption="This is my image")

st.audio("sample-6s.mp3")

st.video("sample-5s.mp4")

# st.image("sample-boat-400x300.png", caption="This is my image")