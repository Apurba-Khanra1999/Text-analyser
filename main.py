import streamlit as st
import subprocess
import sys

st.set_page_config(
    page_title="Text Analyzer",
    page_icon="✅",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.logo(icon_image="logo.png", image="logo.png")
st.title('Our Products')
col1, col2 =st.columns(2)
with col1:
    with st.container(border=True):
        left, right = st.columns([1,4])
        with left:
            st.image('scan.png', width=30)
        with right:
            st.write('Managing, cleaning and modifying the raw data using various tools provided')
        if st.button("Analyzer Text"):
            st.switch_page("pages/Text Analyzer.py")

with col2:
    with st.container(border=True):
        left, right = st.columns([1,4])
        with left:
            st.image('review.png', width=30)
        with right:
            st.write('AI generated reviews for colleges using College Name')
        if st.button("Give Review"):
            st.switch_page("pages/Review.py")

st.divider()
st.markdown('Feel free to suggest an edit 📝', unsafe_allow_html=True)
st.markdown('📩 Contact me - apurbakhanra09@gmail.com', unsafe_allow_html=True)