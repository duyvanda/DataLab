import streamlit as st
import streamlit.components.v1 as com
import pandas as pd
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np

with open("design.css") as source:
    design = source.read()

com.html(f"""
<div>
<style>
{design}
</style>
<h1 class="heading">
This is heading   
</h1>
</div>     
""")