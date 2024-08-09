import  streamlit as st
import os
import google.generativeai as genai
st.set_page_config(
    page_title="Meta Data",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.page_link("main.py", label="H O M E", icon="🏡")
st.divider()

def main():
    st.subheader('META DATA')
    st.markdown('''
    INFO PAGE - 

Meta Heading - Balurghat College [BC] - Course Admissions 2024, Fees, Review

Meta Description - Check Balurghat College fees, admissions procedure, college review, photos on Sikshapedia for guide to excellence in the educational journey.

Meta Keywords - 
mcn college,
mcn college course admissions,
mcn college cut off,
mcn college placement,
mcn college admission,
mcn college contact number,


------------------------------------------------------------------------------


COURSE AND FEES PAGE - 

Meta Heading - Balurghat College [BC] - Course, Fees, Entrance Exam, Eligibility 2024

Meta Description - Check Balurghat College courses and fee structure 2024-2025. The college offers many degrees with basic entrance exams, syllabus and eligibility.

Meta Keywords - 
mcn college fee,
mcn college fees,
mcn college fee structure,
mcn college fees structure,
mcn college course fees,
mcn college courses,


------------------------------------------------------------------------------

REVIEWS AND RATINGS - 

Meta Heading - Balurghat College [BC] - Campus Reviews and Ratings 2024-2025

Meta Description - Read all the reviews and ratings of Balurghat College about the campus area, hostel, library, admission, facilities. sikshapedia is a review portal for top colleges.

Meta Keywords - 
mcn college reviews,
mcn college review,
mcn college student review,
mcn college ranking,
mcn college student reviews,

------------------------------------------------------------------------------

GALLERY PAGE - 

Meta Heading - Balurghat College [BC] - Campus Photos, Videos and Gallery

Meta Description - View Balurghat College new campus area photos, logo, images hostel rooms, library. Campus gallery of the college at sikshapedia.com.

Meta Keywords - 
mcn college photos,
mcn college images,
mcn college gallery,
    ''')

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