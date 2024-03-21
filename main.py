import streamlit as st
import pandas as pd
import os
import re
from collections import Counter
from datetime import datetime
import streamlit.components.v1 as components

# Function to load existing DataFrame from file
def load_data(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return pd.DataFrame(columns=['Input Text','Date and Time'])

# Function to save DataFrame to file
def save_data(df, file_path):
    df.to_csv(file_path, index=False)

st.set_page_config(
    page_title="Text Analyser",
    page_icon="🪄",
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


# Streamlit app
def main(df):
    st.markdown("<h2 style='text-align: center;'>Text Analyser By Apurba</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        text_input = st.text_area('Paste your text here (Ctrl + Enter)', height=400)
        total_characters = count_characters(text_input)
        total_words = count_words(text_input)
        total_sentences = count_sentences(text_input)
        total_spaces = count_spaces(text_input)
        line_count = count_lines(text_input)

        col3, col4 = st.columns(2)
        with col3:
            st.success(f"Characters : {total_characters}")
            st.info(f"Words: {total_words}")
            st.success(f"Sentences : {total_sentences}")
        with col4:
            st.warning(f"Lines: {line_count}")
            st.error(f"Spaces: {total_spaces}")
        st.markdown("<h4 style='text-align: left;'>Select the number of Top Words</h4>", unsafe_allow_html=True)

        top_words_count = st.slider("", 1, 10, 5)
        top_n_words = top_words(text_input, top_words_count)
        st.subheader(f"Frequently used {top_words_count} Words")
        for word, frequency in top_n_words:
            st.write(f"{word} : {frequency}")
    with col2:
        if text_input:
            lowerCaseCol, commaCol = st.columns(2)
            with lowerCaseCol:
                lowercase_checkbox = st.checkbox("Lowercase all text")
            with commaCol:
                comma_checkbox = st.checkbox("Add comma at the end of each line")
            if lowercase_checkbox:
                text_input = text_input.lower()


            col5, col6 = st.columns(2)
            with col5:
                find_word = st.text_input("Find Word")
            with col6:
                replace_word = st.text_input("Replace it with")
            st.divider()
            processed_text = text_input
            if comma_checkbox:
                processed_text = add_punctuation(processed_text, comma_checkbox)

            # st.subheader("Processed Text:")
            processed_text = find_and_replace(processed_text, find_word, replace_word)
            st.text_area("Processed Text", value=processed_text, height=500)


    if text_input:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_df = pd.DataFrame({'Input Text': [text_input],'Date and Time': [current_time]})
        df = pd.concat([df, new_df], ignore_index=True)
        df = df.tail(10)
        save_data(df, file_path)
        st.success('Text saved successfully!')

    #------------------------------------------------------------------------------------------
    # Define the perplexity URL
    perplexity_url = "https://www.perplexity.ai/"

    # Create a checkbox for perplexity
    show_perplexity = st.checkbox("Show Perplexity")

    # Display the perplexity URL in an iframe if checkbox is selected
    if show_perplexity:
        st.text("⚠️Some websites might not load due to security reasons")
        components.iframe(perplexity_url, scrolling=True, height=800)

    # Display the DataFrame
    st.write('### History:')
    st.write(df[::-1], use_container_width=True)


if __name__ == '__main__':
    file_path = 'saved_text.csv'
    df = load_data(file_path)
    main(df)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
