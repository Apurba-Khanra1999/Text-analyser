import pyperclip
import streamlit as st
import pandas as pd
import os
import re
from collections import Counter
from datetime import datetime
import textwrap as tw
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Easy SEO",
    page_icon="🧿",
    layout="wide",
)

def count_characters(text):
    return len(text)

def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    # Using a simple regex pattern to split sentences
    sentences = re.split(r'[.!?]+', text)
    # Filtering out empty strings (which can happen if there are multiple punctuation marks)
    sentences = [sentence for sentence in sentences if sentence.strip()]
    return len(sentences)

def count_spaces(text):
    # Counting spaces directly
    return text.count(" ")

def count_lines(text):
    # Counting lines by splitting text by '\n' character
    lines = text.split('\n')
    # Removing empty lines
    lines = [line for line in lines if line.strip()]
    return len(lines)

def top_words(text, n=5):
    # Split text into words
    words = re.findall(r'\w+', text.lower())
    # Count word frequencies
    word_freq = Counter(words)
    # Get the top n most common words
    top_n_words = word_freq.most_common(n)
    return top_n_words

def add_punctuation(text, add_comma):
    if add_comma:
        return '\n'.join([line.strip() + ',' for line in text.split('\n') if line.strip()])
    else:
        return text

def find_and_replace(text, find_word, replace_word):
    return re.sub(r'\b{}\b'.format(find_word), replace_word, text)

# Function to include FontAwesome icon in HTML


# Streamlit app
def main():
    st.sidebar.subheader("Crafted with 💖 by Apurba")
    st.sidebar.markdown("<h1 style='text-align: center; font-size: 40px'>Smart Text</h1>", unsafe_allow_html=True)
    lowerCaseCol, commaCol = st.columns(2)
    with lowerCaseCol:
        lowercase_checkbox = st.checkbox("All text to Lowercase")
    with commaCol:
        comma_checkbox = st.checkbox("Comma at end of each line")

    # st.markdown("<h3 style='text-align: center; font-size: 22px'>Find and Replace</h3>", unsafe_allow_html=True)
    col5, col6 = st.columns(2)
    with col5:
        find_word = st.text_input("Find Word")
    with col6:
        replace_word = st.text_input("Replace it with")
    col1, col2 = st.columns([1,2])

    with col1:
        st.subheader('Playground')
        text_input = st.text_area('Paste your text here (Ctrl + Enter)', height=500)
        total_characters = count_characters(text_input)
        total_words = count_words(text_input)
        total_sentences = count_sentences(text_input)
        total_spaces = count_spaces(text_input)
        line_count = count_lines(text_input)

        with st.sidebar:
            col3, col4 = st.columns(2)
            with col3:
                st.info(f"Words: {total_words}")
                st.warning(f"Sentences : {total_sentences}")
            st.success(f"Characters: {total_characters}")
            with col4:
                st.success(f"Lines: {line_count}")
                st.error(f"Spaces: {total_spaces}")

    st.divider()
    processed_text = text_input
    if text_input:
        processed_text = find_and_replace(processed_text, find_word, replace_word)
        if lowercase_checkbox:
            processed_text = processed_text.lower()

        if comma_checkbox:
            processed_text = add_punctuation(processed_text, comma_checkbox)


        with st.sidebar:
            st.divider()
            top_words_count = st.slider("Select the number of Top Words", 1, 10, 3)
            top_n_words = top_words(text_input, top_words_count)
            st.subheader(f"Frequently used {top_words_count} Words")
            for word, frequency in top_n_words:
                st.write(f"{word} : {frequency}")
    with col2:
        if text_input:
            # processed_text = find_and_replace(processed_text, find_word, replace_word)
            # st.text_area("Processed Data", value=processed_text, height=500)
            st.subheader('Processed Text')
            st.code(processed_text, language="None", line_numbers=True)
            # st.code("\n".join(tw.wrap(processed_text)), language="None", line_numbers=True)





if __name__ == '__main__':
    main()

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

css = '''
<style>
    [data-testid="ScrollToBottomContainer"] {
        overflow: hidden;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)
