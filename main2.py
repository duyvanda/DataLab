import streamlit as st
import pandas as pd


def change():
    print(st.session_state.checker)

def on_click():
    print(st.session_state.checker)

checkbox = st.checkbox("Checkbox", value=True, on_change=change, key="checker")
radio = st.radio("Which country do you live", options=("Vietnam", "Trung Quoc"))
btn = st.button("Click me", on_click=on_click)
select = st.selectbox("Select", options=("Vietnam", "Trung Quoc"))
multiselect = st.multiselect("Multi", options=("Vietnam", "Trung Quoc"))

st.write(multiselect)

if checkbox:
    st.write("hi")
else:
    pass