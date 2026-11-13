import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header('My First Streamlit App')
st.subheader('Welcome to my first web application!')
st.markdown('This web is created for practicing the print commands in **Streamlit**')
List = ['Name: Somchai Chaidee','Age: 25 Years old','Status: Learning Python']
st.write("### ข้อมูลส่วนตัว (จาก List):")
for item in List:
    st.write(f"- {item}")