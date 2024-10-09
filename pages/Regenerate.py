import  streamlit as st
import os
import google.generativeai as genai
st.set_page_config(
    page_title="Review",
    page_icon="✅",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.page_link("main.py", label="H O M E", icon="🏡")
st.divider()

genai.configure(api_key="AIzaSyCxlDM0Q-7ROBMgl6wKAM0OGNDlCdrGavE")
# AIzaSyABk1L3eNxv4D9SjtFLcjw3nqKv1Nd19-U             -- SAGNIK
# AIzaSyDXtaS6UDtw5rJo2sk9gUk_I59kcp7TUS0             -- ME
# AIzaSyCxlDM0Q-7ROBMgl6wKAM0OGNDlCdrGavE             -- Alternate

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)
keywords = st.text_area('Enter Keywords (comma-separated)', placeholder='e.g., campus, facilities, placement')
existing_content = st.text_area('Paste Existing Content', placeholder='Paste your existing content here')
chat_session = model.start_chat(
  history=[
  ]
)

if st.button('ReGenerate'):
    st.write(keywords)
    st.write(existing_content)
    response = chat_session.send_message(f'You are an expert content writer.Rewrite this existing paragraph - {existing_content} including the mentioned keywords - {keywords}.Do not make points.')
    st.header('Re Generated Text')
    st.write(response.text)
