import streamlit as st
import pandas as pd

df = pd.read_excel('TODO.xlsx')
df['削除'] = False
df = st.data_editor(df)

def delete():
    global df
    df = df[df['削除'] != True].drop('削除', axis=1)
    df.to_excel('TODO.xlsx', index=False)

clicked = st.button('削除', type='primary', on_click=delete)

if (clicked): st.switch_page('index.py')
