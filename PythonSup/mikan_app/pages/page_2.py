import streamlit as st

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