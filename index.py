import streamlit as st
import pandas as pd

df = pd.read_excel('TODO.xlsx')

st.dataframe(df)

