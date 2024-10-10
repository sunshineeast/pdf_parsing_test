import streamlit as st
import pandas as pd
import pdftotext
from streamlit_pdf_viewer import pdf_viewer
from io import StringIO
# !sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev

st.set_page_config(
    page_title="Analysis",
    # page_icon="👋",
    layout='wide')

# title
st.markdown("<h1 style='text-align: center; font-size: 70px;color: black;letter-spacing: 4px;'>PDF Parsing</h1>", unsafe_allow_html=True)

with st.container(border=True):
    st.session_state.uploaded_file = st.file_uploader('Choose your **.pdf** file to upload', type="pdf")

    if st.session_state.uploaded_file is not None:
        st.success("File is uploaded")

if st.session_state.uploaded_file:
    st.session_state.doc_parsed = st.session_state.uploaded_file.getvalue()
    # st.session_state.doc_parsed = StringIO(st.session_state.uploaded_file.getvalue().decode("utf-8"))
    # st.session_state.doc_parsed = StringIO(st.session_state.uploaded_file.getvalue())
    with st.expander("Click to View file"):
        st.write(st.session_state.doc_parsed)

    # (pdf viewing) works 
    # pdf_viewer(input=st.session_state.doc_parsed, width=700)
    

    # st.session_state.pdf = pdftotext.PDF("sample_pdfs/Nonlinear_Optimization_in_R_using_nlopt.pdf",physical=True)

    # this works but need to reboot app everytime I make change in code
    # with open("sample_pdfs/Nonlinear_Optimization_in_R_using_nlopt.pdf", "rb") as f:
    #     st.session_state.pdf = pdftotext.PDF(f,physical=True)

    # Not working on streamlit but working on google colab
    with open(st.session_state.st.session_state.uploaded_file, "rb") as f:
        st.session_state.pdf = pdftotext.PDF(f,physical=True)
    
    for st.session_state.page in st.session_state.pdf:
        st.write(st.session_state.page)

    
