import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to fetch metadata from the URL
def fetch_metadata(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'No title found'
        description = soup.find('meta', attrs={'name': 'description'})

        if description:
            description = description.get('content', 'No description found')
        else:
            description = 'No description found'

        return title, description
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching metadata: {e}")
        return None, None

# Function to validate length of title and description
def validate_length(title, description):
    title_max_length = 60
    description_max_length = 160

    title_status = f"Title Length: {len(title)} / {title_max_length} characters"
    description_status = f"Description Length: {len(description)} / {description_max_length} characters"

    return title_status, description_status

# Streamlit App Layout
st.title("Google Title & Meta Description Length Tester")

# Input Section
url = st.text_input("Enter URL", "")
manual_title = st.text_input("Enter Title (Optional)", "")
manual_description = st.text_area("Enter Meta Description (Optional)", height=100)
generate = st.button("GENERATE PREVIEW")

if generate:
    title, description = None, None

    if url:
        title, description = fetch_metadata(url)

    # If user provided manual input, prioritize it over fetched data
    title = manual_title if manual_title else title
    description = manual_description if manual_description else description

    if title and description:
        # Create two columns
        col1, col2 = st.columns(2)
        with col1:
            # Display Desktop Result Preview
            st.subheader("Typical Desktop Result")
            st.write(f"**URL:** {url}")
            st.markdown(f"**Title:** <span style='color:#E5E4E2; font-size:18px;'>{title}</span>", unsafe_allow_html=True)
            st.write(f"**Description:** {description}")

        with col2:
            # Display Mobile Result Preview
            st.subheader("Typical Mobile Result")
            st.markdown(f"**URL:** {url}")
            st.markdown(f"**Title:** <span style='color:#E5E4E2; font-size:16px;'>{title}</span>", unsafe_allow_html=True)
            st.write(f"**Description:** {description}")

        # Display alerts for title and description length
        title_status, description_status = validate_length(title, description)
        st.write(f"**{title_status}**")
        st.write(f"**{description_status}**")

        if len(title) > 60:
            st.warning("Title is too long! Try to keep it under 60 characters.")
        if len(description) > 160:
            st.warning("Description is too long! Try to keep it under 160 characters.")
    else:
        st.error("Please enter a valid URL or manually input the title and description.")

