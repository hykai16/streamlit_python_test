import streamlit as st
from PIL import Image

st.title('みかんのホームページ')
st.caption('ここはみかんがハッピーになるページです。')

image = Image.open('./pages/data/きょむりん.jpg')
st.image(image, width=200)

video_file = open('./pages/data/にゃんにゃん.mp4','rb')
video_bytes = video_file.read()
st.video(video_bytes)