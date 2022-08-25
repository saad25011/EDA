from enum import auto
from turtle import width
import pandas as pd
import seaborn as sns
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from PIL import Image

image = Image.open('laptop1.jpg')

st.markdown("<h3 style='text-align: center; color: #0E0752; letter-spacing :2cm ;font-size :3cm ;font-family:Display fonts'>|EDA|</h3>", unsafe_allow_html=True)

with st.sidebar.header("Choose the number of rows to show"):
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    st.sidebar.markdown("<h3 style='text-align: center; color: blue '>EDA APP</h3>", unsafe_allow_html=True)
    st.sidebar.image(image, caption='Sunrise by the mountains', use_column_width=True)
if uploaded_file is not None:
    def load_csv():
        data = pd.read_csv(uploaded_file)
        return data 
    df = load_csv()
    report = ProfileReport(df , explorative=True)
    st.write(df, width= 20000)
    st.markdown("<h3 style='text-align: center; color: darkblue; letter-spacing :2cm ;font-size :3cm ;font-family:Display fonts'>Report</h3>", unsafe_allow_html=True)
    st_profile_report(report)
    st.write('---')



