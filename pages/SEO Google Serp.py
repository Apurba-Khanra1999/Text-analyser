import streamlit as st
import requests
from bs4 import BeautifulSoup
import csv
from io import StringIO

# --- Config ---
st.set_page_config(page_title="SEO Google Serp Optimizer", layout="centered")
INDIGO = "#4B0082"

# --- Styles ---
st.markdown(
    f"""
    <style>
        body {{
            background-color: #f3f4f6;
        }}
        .title {{
            font-size: 2rem;
            color: {INDIGO};
            margin-bottom: 1rem;
        }}
        .snippet {{
            border: 1px solid #ccc;
            padding: 1rem;
            border-radius: 8px;
            background-color: white;
            margin-bottom: 1rem;
        }}
        .google-preview {{
            background: #fff;
            border-radius: 8px;
            padding: 1rem;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
            max-width: 600px;
        }}
        .google-preview-title {{
            font-size: 18px;
            color: #1a0dab;
        }}
        .google-preview-url {{
            font-size: 14px;
            color: #006621;
        }}
        .google-preview-desc {{
            font-size: 14px;
            color: #545454;
        }}
        .mobile {{
            max-width: 360px !important;
        }}
        .switch {{
            margin: 1rem 0;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title ---
st.markdown(f"<div class='title'>🔍 SEO Google Serp Optimizer</div>", unsafe_allow_html=True)

# --- URL Input ---
url = st.text_input("🔗 Enter URL to fetch snippet", "")

def fetch_metadata(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else ""
        desc_tag = soup.find("meta", attrs={"name": "description"})
        description = desc_tag["content"].strip() if desc_tag and "content" in desc_tag.attrs else ""

        return title, description
    except:
        return "", ""

if url:
    title_fetched, desc_fetched = fetch_metadata(url)
else:
    title_fetched, desc_fetched = "", ""

# --- Editable Inputs (no char limit) ---
title = st.text_area("📝 Title (Recommended: 60–70 characters, ≤ 580px)", value=title_fetched, height=70)
desc = st.text_area("📝 Meta Description (Recommended: 150–160 characters, 430–920px)", value=desc_fetched, height=100)

# --- Character & Pixel Calculations ---
def pixel_width(text, px_per_char):
    return int(len(text) * px_per_char)

title_chars = len(title)
title_pixels = pixel_width(title, 7.1)
desc_chars = len(desc)
desc_pixels = pixel_width(desc, 6.1)

# --- Feedback ---
st.write(f"📏 **Title:** {title_chars} characters | {title_pixels}px")
st.progress(min(title_pixels / 580, 1.0))

st.write(f"📏 **Description:** {desc_chars} characters | {desc_pixels}px")
st.progress(min(desc_pixels / 920, 1.0))

# --- Truncate Preview Logic ---
def truncate_by_pixel(text, max_px, px_per_char):
    max_chars = int(max_px // px_per_char)
    return text if pixel_width(text, px_per_char) <= max_px else text[:max_chars - 3] + "..."

# --- Desktop/Mobile Preview Toggle ---
preview_mode = st.radio("🖥️ Choose Preview Mode", ["Desktop", "Mobile"], horizontal=True)
preview_class = "google-preview"
if preview_mode == "Mobile":
    preview_class += " mobile"

# --- Google Preview ---
st.markdown(f"""
<div class='{preview_class}'>
    <div class='google-preview-url'>{url or 'www.example.com'}</div>
    <div class='google-preview-title'>{truncate_by_pixel(title, 580, 7.1)}</div>
    <div class='google-preview-desc'>{truncate_by_pixel(desc, 920, 6.1)}</div>
</div>
""", unsafe_allow_html=True)

# --- Export CSV ---
if st.button("📥 Export as CSV"):
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["URL", "Title", "Description", "Title Characters", "Description Characters"])
    writer.writerow([url, title, desc, title_chars, desc_chars])
    st.download_button("Download CSV", data=output.getvalue(), file_name="seo_snippet.csv", mime="text/csv")
