import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image



# ------------------------------------------------------------------------

# st.title('Streamlit 超入門')
# st.write('Display Image')

# option = st.selectbox(
#     'あなたが好きな数字を教えてください、',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、', option, 'です。'


# if st.checkbox('Show Image'):
#     img = Image.open('SampleImage_Lena.jpg')
#     st.image(img, caption='Lena', use_column_width=True)

# st.write('Interactive Widgets')
# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味：', text

# condition = st.slider('あなたの今の調子は？',0, 100, 50)
# 'コンディション：', condition


# ------------------------------------------------------------------------

# st.title('Streamlit 超入門')
# st.sidebar.write('◇Interactive Widgets')

# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？',0, 100, 50)
# 'コンディション：', condition

# ------------------------------------------------------------------------


# st.title('Streamlit 超入門')
# st.write('Interactive Widgets')

# left_column, right_column = st.columns(2)
# button = left_column.button('右カラム文字を表示')


# if button:
#     right_column.write('ここは右カラム')

# expander1 = st.expander ('問い合わせ1')
# expander1.write('問い合わせ1の回答')
# expander2 = st.expander ('問い合わせ2')
# expander2.write('問い合わせ2の回答')
# expander3 = st.expander ('問い合わせ3')
# expander3.write('問い合わせ3の回答')

# ------------------------------------------------------------------------

import time

st.title('Streamlit 超入門')
st.write('プレグレスバーの表示')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Interation {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'








