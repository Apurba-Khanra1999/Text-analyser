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
col1, col2, col3 =st.columns(3)
col4, col5, col6 =st.columns(3)
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
with col3:
    with st.container(border=True):
        left, right = st.columns([1,4])
        with left:
            st.image('generate.png', width=30)
        with right:
            st.write('Generate Blogs based on Keywords.')
        if st.button("Generate"):
            st.switch_page("pages/Write Blogs.py")
with col4:
    with st.container(border=True):
        left, right = st.columns([1,4])
        with left:
            st.image('seo.png', width=30)
        with right:
            st.write('Generate Meta Title, Description and Keywords.')
        if st.button("Get Data"):
            st.switch_page("pages/College SEO Generator.py")

with col5:
    with st.container(border=True):
        left, right = st.columns([1,4])
        with left:
            st.image('google.png', width=30)
        with right:
            st.write('Generate Google SEO Serp Preview with validation.')
        if st.button("Preview"):
            st.switch_page("pages/SEO Google Serp.py")



st.divider()
st.markdown('Feel free to suggest an edit 📝', unsafe_allow_html=True)
st.markdown('📩 Contact me - apurbakhanra09@gmail.com', unsafe_allow_html=True)