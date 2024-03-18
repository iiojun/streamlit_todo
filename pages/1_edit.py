import streamlit as st
import pandas as pd

df = pd.read_excel('TODO.xlsx')
df = st.data_editor(df)

clicked = st.button('保存', type='primary',
             on_click=lambda: df.to_excel('TODO.xlsx', index=False))

if (clicked): st.switch_page('index.py')
