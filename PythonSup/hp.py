import streamlit as st
from PIL import Image

st.title('みかんのホームページ')
st.caption('ここはみかんがハッピーになるページです。')

st.subheader('自己紹介')
st.text('田村ゆかりさんとねこが大好きな、アラサープログラミング講師です')
code = '''
import streamlit as st

st.title('サプーアプリ')
'''
st.code(code,language='python')

image = Image.open('mikan_app/pages/data/きょむりん.jpg')
st.image(image, width=200)

video_file = open('mikan_app/pages/data/にゃんにゃん.mp4','rb')
video_bytes = video_file.read()
st.video(video_bytes)

#何かの処理の開始時と終了時に必須の処理を、絶対に実行してくれるwith構文
with st.form(key='profile_form'):

    name = st.text_input('Name')
    address = st.text_input('住所')

    age_category = st.selectbox(
        '年齢層',
    ('子ども（18歳未満）','大人（18歳以上）'))

    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'ようこそ！{name}さん！{address}に書類を送りました！')
