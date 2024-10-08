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
# AIzaSyBd8NKxdnGAY7vu7qrNqNnOZaVj0Reh6eU             -- Sukanta
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
collegeName = st.text_input('Enter a College Name', placeholder='Narula Institutue Of Technology')
chat_session = model.start_chat(
  history=[
  ]
)

if st.button('Generate'):
  response = chat_session.send_message(f'Create a one liner student review title for {collegeName} in which he/she is studying in simple english')
  responseDes = chat_session.send_message(f'I want you to act as a student of {collegeName}.Create a organic student review based on facilities, campus, placements, fees and admission within 100 words.')
  Col1,Col2 = st.columns(2)
  with Col1:
    st.header('Review Title')
    st.write(response.text)
  with Col2:
    st.header('Review Description')
    st.write(responseDes.text)
