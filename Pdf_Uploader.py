import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader
a = st.file_uploader(label= "Uploade a file")
if a:   
    pdf = PdfReader(a)
    b = ""
    for i in range(len(pdf.pages)):
        b =b+(pdf.pages[i].extract_text()) +" "

    genai.configure(api_key= "AIzaSyCSjm9BHbo5hJIHf_Pe80cgisSGXpdVPCA")
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = "Now your are the pdf summarizer.read the entire content and provide a cleare summary"
    responce = model.generate_content(prompt +b)
    if st.button("provide summary"):
        st.write(responce.text)
