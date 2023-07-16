import streamlit as st
import pandas as pd

table = pd.DataFrame({"Col1":[1,2,3], "Col2":[4,5,6]})

st.title("Hi I am streamlit app")

st.subheader("I am sub headers")

st.header("I am headers")

st.text("I am text")

st.markdown("**I love you** and my *famil*")

# cheat sheet here https://www.markdownguide.org/cheat-sheet/

st.markdown("[google](https://www.google.com)")

st.markdown("---")

st.caption("Hi am caption")

# https://katex.org/docs/supported.html

st.latex(r"\def\sqr#1{#1^2} \sqr{y}")

json = {"a":1, "b":2}
st.json(json)

code = \
"""
def func():
    print("Ly")
"""
st.code(code, language="python")

st.metric(label="Sales", value="600M", delta="60%")

st.metric(label="Debt", value="700M", delta="-10%")

st.table(table)