
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title(' streamlit 超入門')

st.write('プレぐれすばーの表示')
'start'

latest_iteration = st.empty()

bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!'

left_col, right_col = st.columns(2)
button = left_col.button('右カラムに文字を表示')
if button & 1:
    right_col.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

condition  = st.slider('体調は？', 0, 100, 50)
text = st.text_input('あなたの趣味は？')

'趣味：',text
'体調：',condition

#if st.checkbox('Show Image'):
img = Image.open('Moz.jpg')
st.image(img, caption = 'Moz', use_column_width = True)



