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

genai.configure(api_key="AIzaSyBd8NKxdnGAY7vu7qrNqNnOZaVj0Reh6eU")
# AIzaSyABk1L3eNxv4D9SjtFLcjw3nqKv1Nd19-U             -- SAGNIK
# AIzaSyDXtaS6UDtw5rJo2sk9gUk_I59kcp7TUS0             -- ME
# AIzaSyBd8NKxdnGAY7vu7qrNqNnOZaVj0Reh6eU             -- Sukanta
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 10000,
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)
keywords = st.text_area('Paste your keywords', placeholder='college,faculty,placements,students')
chat_session = model.start_chat(
  history=[
  ]
)

if st.button('Generate'):
  response = chat_session.send_message(f'You are an experienced SEO analyst and content writer. Write a complete descriptive blog post with proper blog post title. Include the mentioned keywords - {keywords}. Make the keywords bold in the blogpost.')
  st.header('Blog')
  st.write(response.text)
