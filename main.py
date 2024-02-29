import streamlit as st
import re
from collections import Counter

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


def top_words(text, n=5):
    # Split text into words
    words = re.findall(r'\w+', text.lower())
    # Count word frequencies
    word_freq = Counter(words)
    # Get the top n most common words
    top_n_words = word_freq.most_common(n)
    return top_n_words


def add_punctuation(text, selected_punctuation):
    if not selected_punctuation:
        return text
    else:
        return '\n'.join([line.strip() + ',' for line in text.split('\n') if line.strip()])


def main():
    # st.header("Text Analyzer")
    st.markdown("<h1 style='text-align: center;'>Text Analyser</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns([4, 2])

    with col1:
        text_input = st.text_area('Paste your text here (Ctrl + Enter)', height=550)

    with col2:
        if text_input:
            top_words_count = st.slider("Select the number of top words to show", 1, 10, 5)
            total_characters = count_characters(text_input)
            total_words = count_words(text_input)
            total_sentences = count_sentences(text_input)
            total_spaces = count_spaces(text_input)

            col3, col4 = st.columns(2)
            with col3:
                st.success(f"Characters : {total_characters}")
                st.info(f"Words: {total_words}")
            with col4:
                st.warning(f"Sentences: {total_sentences}")
                st.error(f"Spaces: {total_spaces}")

            punctuation_options = ['Comma (,)', 'Period (.)', 'Semicolon (;)', 'Exclamation (!)', 'Question Mark (?)']
            selected_punctuation = st.multiselect("Select punctuation to add at the end of each line:", punctuation_options)

            processed_text = add_punctuation(text_input, selected_punctuation)

            st.subheader("Processed Text:")
            st.text_area("Processed Text", value=processed_text, height=500)


if __name__ == "__main__":
    main()

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
