import streamlit as st
import pandas as pd
import datetime
import os
import pdftotext

st.set_page_config(
    page_title="Health Quant Analysis",
    # page_icon="👋",
    layout='wide',
)

def v_spacer(height, sb=False) -> None:
    for _ in range(height):
        if sb:
            st.sidebar.write('\n')
        else:
            st.write('\n')

# os.chdir('V:/1. R & Python work/Python/2.AnalytixLabs Practice/Health pdf parser llma modules')


# title
st.markdown("<h1 style='text-align: center; font-size: 70px;color: black;letter-spacing: 4px;'>PDF Parsing</h1>", unsafe_allow_html=True)

with st.container(border=True):

    st.write("Note: Upload pdf files one by one. When one is Parsed & Processed then only upload another.")
    st.session_state.uploaded_file = st.file_uploader('Choose your **.pdf** file to upload', type="pdf")

    if st.session_state.uploaded_file is not None:
        # st.write(st.session_state.uploaded_file.name)
        st.success("File is uploaded")

if st.session_state.uploaded_file:

# with open('doc_parsed.pickle', 'rb') as f:
#     st.session_state.doc_parsed = pickle.load(f)

# st.header("Welcome to the Multipage App! 👋")


########################### 1 - directly using uploaded file ###############################


    st.session_state.doc_parsed = st.session_state.uploaded_file.getvalue()

    with open(st.session_state.doc_parsed, "rb") as f:
        st.session_state.pdf = pdftotext.PDF(f)

    st.write(st.session_state.st.session_state.pdf)

    
    # st.snow()
    # st.success('Parsing is Complete')  
    # st.write(st.session_state.doc_parsed)