import streamlit as st
import pandas as pd

df = pd.read_excel('TODO.xlsx')

title = st.text_input(label='タイトル')
memo = st.text_area(label='内容')
date = st.date_input(label='締切')
done = False

def append():
    global df
    df_new = pd.DataFrame({'タイトル': [title],
                           '内容':     [memo], 
                           '締切':     [date],
                           '実施':     [done]})
    df = pd.concat([df, df_new])
    df.to_excel('TODO.xlsx', index=False)

clicked = st.button('登録', type='primary', on_click=append)

if (clicked): st.switch_page('index.py')
