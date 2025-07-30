import streamlit as st
import io

# --- CONFIG ---
st.set_page_config(page_title="🎓 College SEO Generator", layout="wide")

# --- STYLING ---
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
        }
        .main {
            background: #e8eaf6;
        }
        .section-title {
            font-size: 1.7rem;
            font-weight: 700;
            color: #3f51b5;
            margin-bottom: 0.5rem;
        }
        .meta-box {
            background: white;
            border-left: 5px solid #3f51b5;
            padding: 1rem 1.25rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        }
        .meta-title {
            font-weight: 600;
            color: #1a237e;
        }
        .meta-desc {
            color: #333;
        }
        .stTabs [data-baseweb="tab-list"] {
            overflow-x: auto;
            overflow-y: hidden;
            white-space: nowrap;
            flex-wrap: nowrap !important;
            display: flex;
        }
        .stTabs [data-baseweb="tab-list"] button {
            flex: 0 0 auto;
            font-size: 1rem;
            color: #1a237e;
        }
    </style>
""", unsafe_allow_html=True)


# --- INPUT HEADER ---
st.markdown('<div class="section-title">🎓 College SEO Content Generator</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])  # Adjust ratio if needed

with col1:
    college_name = st.text_input("🏫 College Name", value="ABC Institute of Technology")

with col2:
    year = st.text_input("📅 Year", value="2025")

# Generate short form of college name (e.g., "ABC Institute of Technology" -> "AIT")
def get_short_form(name):
    return ''.join(word[0].upper() for word in name.split())

short_form = get_short_form(college_name)

# --- PLACEHOLDER REPLACEMENT ---
def replace_placeholders(text, name, short, year_val):
    text = text.replace("Balurghat university [BC]", f"{name} [{short}]")
    text = text.replace("Balurghat university", name)
    text = text.replace("(College Name)", name)
    text = text.replace("(Colleges Name)", name)
    text = text.replace("2025", year_val)
    return text

# --- DATA SOURCE ---
sections = {
    "📘 Info": {
        "Meta Title": ["Balurghat university - Course Admissions, Fees, Review"],
        "Meta Description": [
            "Check Balurghat university fees, admissions procedure, university review, photos on Sikshapedia for guide to excellence in the educational journey."
        ]
    },
    "📚 Course & Fees": {
        "Meta Title": ["Balurghat university [BC] - Course Fees, Entrance Exam, Eligibility"],
        "Meta Description": [
            "Check Balurghat university courses and fee structure. The university offers many degrees with basic entrance exams, syllabus and eligibility."
        ]
    },
    "⭐ Reviews": {
        "Meta Title": ["Balurghat university [BC] - Reviews, Rating of Campus"],
        "Meta Description": [
            "Read all the reviews and ratings of Balurghat university about the campus area, hostel, library, admission, facilities. sikshapedia is a review portal for top universities."
        ]
    },
    "🖼️ Gallery": {
        "Meta Title": ["Balurghat university [BC] - New Campus Photos, Videos"],
        "Meta Description": [
            "View Balurghat university new campus area photos, logo, images hostel rooms, library. Campus gallery of the university at sikshapedia.com."
        ]
    },
    "🎓 Scholarships": {
        "Meta Title": ["Balurghat university Scholarships : Eligibility and Details"],
        "Meta Description": [
            "Explore Balurghat university Kolkata scholarships, including eligibility and application deadlines, at Sikshapedia."
        ]
    },
    "🎯 Admission": {
        "Meta Title": [
            "(College Name) Admissions 2025: Dates, Fees, Eligibility, Application Process, Selection Criteria, Cutoff, Application & Selection, Application Form, Courses, Fees & Eligibility, Ranking, Placement"
        ],
        "Meta Description": [
            "Discover essential details about (College Name) Admission 2025, including fees, eligibility, and application processes. Visit Sikshapedia for comprehensive insights.",
            "Get all the information you need for (College Name) Admission 2025, from fees to selection criteria. Explore Sikshapedia for expert guidance and updates.",
            "Planning for (College Name) Admission 2025? Find crucial details on fees, eligibility, and application steps at Sikshapedia. Your journey starts here!"
        ],
        "Keywords": ["admission college, admission open, admission open 2025-26, admission open 2025-26 West Bengal, colleges admission, (Colleges Name) course admission 2025, (Colleges Name) admission process, (Colleges Name) Admission Process 2025, eligibility criteria for (Colleges Name), criteria for admission in (Colleges Name), (Colleges Name) official website, admission 2025 college, (course name) admission 2025 college, (Colleges Name) entrance exam, (Colleges Name) admission, (Colleges Name) course admissions, (Colleges Name) entrance exam 2025, (Colleges Name) direct admission, (Colleges Name) admission 2025-26, (Colleges Name) fee structure"]

    },
    "📉 Cutoff": {
        "Meta Title": [
            "(Colleges Name) Cutoff 2025: Check WBJEE Previous Years Cutoff Ranks",
            "(Colleges Name) Cutoff 2025: Check Category and Year-wise Cutoff",
            "(Colleges Name) Cutoff 2025: Check Previous Year’s Closing Cut Off Score/Trends"
        ],
        "Meta Description": [
            "Discover the WBJEE cutoff ranks for 2025 at (College Name). Explore previous years' data and make informed decisions for your college applications at Sikshapedia.",
            "Stay updated on (College Name) Cutoff 2025! Check WBJEE previous years' cutoff ranks to guide your college choices. Visit Sikshapedia for detailed insights.",
            "Navigate your college journey with (College Name) Cutoff 2025. Access WBJEE previous years' cutoff ranks and enhance your application strategy at Sikshapedia.",
            "Discover the 2025 cutoff for (College Name) by category and year. Visit Sikshapedia for detailed insights and stay informed about your admission prospects.",
            "Explore the 2025 cutoff trends for (Colleges Name) across various categories. Visit Sikshapedia for comprehensive details and enhance your admission strategy."
        ],
        "Keywords":["admission college, (Colleges Name) cutoff, (Colleges Name) wbjee cut off, (Colleges Name) cut off wbjee, (Colleges Name) cutoff 2023, wbjee cutoff for (Colleges Name), (Colleges Name) cutoff marks, wbjee cutoff 2025"]
    },
    "💼 Placement": {
        "Meta Title": ["(Colleges Name) Placement 2025: Highest Package, Average Package, Top Recruiters, Offers Made"],
        "Meta Description": [
            "Discover the 2025 placement statistics for (College Name): explore highest and average packages, top recruiters, and offers made. Visit Sikshapedia now!",
            "Uncover the latest placement insights for (College Name) in 2025, including highest and average packages, top recruiters, and job offers. Learn more at Sikshapedia!",
            "Explore (College Name) Placement 2025: Find details on highest and average packages, top recruiters, and offers made. Visit Sikshapedia for comprehensive insights!"
        ],
        "Keywords": ["Admission college, (Colleges Name) Placement, (Colleges Name) Highest Package, (Colleges Name) Average Package, (Colleges Name) Top Recruiters, (Colleges Name) Placement Report, (Colleges Name) Placement Percentage, (Colleges Name) Placement News, (Colleges Name) Placement Companies List, Lowest Package of (College Name)"]
    },
    "👨‍🏫 Faculty": {
        "Meta Title": [
            "(Colleges Name) Faculty: Reviews, Experience, Strength & Teaching methodology",
            "(Colleges Name) Facilities Details: Hostel, Campus, Infrastructure, Library, Canteen"
        ],
        "Meta Description": [
            "Discover in-depth reviews and insights on (College Name) Faculty, including teaching methodologies and strengths. Visit Sikshapedia for comprehensive information.",
            "Explore the strengths and teaching methods of (College Name) Faculty through detailed reviews and experiences. Find out more at Sikshapedia today!",
            "Uncover the unique teaching methodologies and strengths of (College Name) Faculty. Read reviews and experiences on Sikshapedia for valuable insights."
        ],
        "Keywords":["admission college, nursing colleges West Bengal Faculty, nursing colleges West Bengal faculty list, private nursing colleges West Bengal faculty, GNM nursing colleges West Bengal faculty, nursing colleges West Bengal faculty 2025, nursing colleges West Bengal faculty fees, West Bengal private nursing college list, list of nursing colleges in West Bengal"]
    },
    "📰 News & Articles": {
        "Meta Title": ["(Colleges Name) News and Latest Updates 2025"],
        "Meta Description": [
            "Stay informed with the latest news and updates from (College Name) for 2025. Visit Sikshapedia for comprehensive insights and essential information.",
            "Discover the latest updates and news from (College Name) for 2025. Explore Sikshapedia for in-depth articles and essential resources.",
            "Get the latest news and updates on (College Name) for 2025. Visit Sikshapedia for valuable insights and information to stay ahead."
        ],
        "Keywords":["Admission college, nursing colleges West Bengal News & Articles, private nursing colleges West Bengal news & articles, GNM nursing colleges West Bengal news & articles, nursing colleges West Bengal news & articles 2025, government nursing colleges West Bengal news & articles, nursing colleges West Bengal news & articles 2025"]
    },
    "🏨 Hostel": {
        "Meta Title": ["(College Name) Hostel Fees 2025, Facilities, Rooms, Food, Photos"],
        "Meta Description": [
            "Discover the 2025 hostel fees at (College Name), along with details on facilities, rooms, food, and photos. Visit Sikshapedia for comprehensive insights.",
            "Explore (College Name) hostel fees for 2025, including amenities, room options, dining, and photos. Get all the details at Sikshapedia today!",
            "Find out about (College Name) hostel fees for 2025, featuring facilities, room types, food options, and photos. Visit Sikshapedia for more information!"
        ],
        "Keywords":["admission college, nursing colleges West Bengal hostel fees, GNM nursing colleges West Bengal hostel, government nursing colleges West Bengal hostel, private nursing colleges West Bengal hostel, nursing colleges West Bengal hostel fee structure, nursing colleges West Bengal hostel open now, West Bengal government male nursing college list, West Bengal nursing hostel, West Bengal private nursing college list, West Bengal male nursing college list, nursing college Howrah West Bengal"]
    },
    "❓ Q&A": {
        "Meta Title": ["(College Name) Q&A on Cutoffs, Placements, Fees & Admission"],
        "Meta Description": [
            "Explore comprehensive Q&A on cutoffs, placements, fees, and admissions for colleges. Visit Sikshapedia for detailed insights and make informed decisions.",
            "Get all your questions answered about college cutoffs, placements, fees, and admissions. Visit Sikshapedia for expert guidance and valuable information.",
            "Discover essential information on college cutoffs, placements, fees, and admissions. Visit Sikshapedia for a thorough Q&A to aid your academic journey."
        ],
        "Keywords": ["admission college, Best nursing colleges q&a, Government nursing colleges q&a, Student nursing interview questions and answers, Nursing colleges q&a fees, GNM nursing interview questions and answers, nursing colleges in west bengal list, nursing colleges in west bengal, nursing college kolkata west bengal, nursing colleges west bengal Q&A, private nursing colleges west bengal q&a, list of nursing colleges west bengal q&a, nursing colleges west bengal q&a fees, west bengal private nursing college list"]
    },
    "🏆 Ranking": {
        "Meta Title": ["(College Name) Ranking 2025: Check Year-wise National Rankings Here"],
        "Meta Description": [
            "Discover the latest 2025 college rankings at Sikshapedia. Explore year-wise national rankings and find the best institutions for your academic journey.",
            "Stay updated with the 2025 college rankings on Sikshapedia. Access comprehensive year-wise national rankings to guide your educational choices.",
            "Explore Sikshapedia for the 2025 college rankings. Check year-wise national rankings and make informed decisions about your higher education path."
        ],
        "Keywords": ["admission college, nursing colleges ranking, nursing colleges ranking in india, bsc nursing colleges ranking, best nursing colleges ranking, nirf ranking 2024 nursing colleges, nirf ranking nursing colleges, ranking of nursing colleges in west bengal, top ranking nursing colleges in india, nirf ranking 2025 nursing colleges, ranking of nursing colleges in kolkata"]
    }
}


# Store edited content
edited_data = {}

# --- DISPLAY TABS ---
tabs = st.tabs(list(sections.keys()))
for tab, (section, content) in zip(tabs, sections.items()):
    with tab:
        st.markdown(f'<div class="section-title">{section}</div>', unsafe_allow_html=True)

        edited_data[section] = {"Meta Title": [], "Meta Description": [], "Keywords": ""}

        for i, title in enumerate(content["Meta Title"], 1):
            title_val = replace_placeholders(title, college_name, short_form, year)
            edited_title = st.text_input(f"✏️ Meta Title {i}", value=title_val, key=f"{section}_title_{i}")
            edited_data[section]["Meta Title"].append(edited_title)

        for j, desc in enumerate(content["Meta Description"], 1):
            desc_val = replace_placeholders(desc, college_name, short_form, year)
            edited_desc = st.text_area(f"📝 Meta Description {j}", value=desc_val, height=100, key=f"{section}_desc_{j}")
            edited_data[section]["Meta Description"].append(edited_desc)

        # Handle keywords with placeholder replacement
        keywords_list = content.get("Keywords", [])
        keywords_text = ", ".join([replace_placeholders(k, college_name, short_form, year) for k in keywords_list])
        edited_keywords = st.text_area("🔑 Keywords", value=keywords_text, height=200, key=f"{section}_keywords")
        edited_data[section]["Keywords"] = edited_keywords

# --- EXPORT BUTTON ---
st.markdown("---")
if st.button("📥 Export All Content as .txt"):
    output = io.StringIO()
    for section, data in edited_data.items():
        output.write(f"### {section}\n")
        for t in data["Meta Title"]:
            output.write(f"Meta Title: {t}\n")
        for d in data["Meta Description"]:
            output.write(f"Meta Description: {d}\n")
        if data["Keywords"]:
            output.write(f"Keywords: {data['Keywords']}\n")
        output.write("\n")

    st.download_button(
        label="Download SEO Content",
        data=output.getvalue(),
        file_name=f"{college_name.replace(' ', '_')}_SEO_Content.txt",
        mime="text/plain"
    )
