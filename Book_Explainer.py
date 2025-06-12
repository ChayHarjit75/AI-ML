import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader
import pyttsx3

voice = pyttsx3.init()

genai.configure(api_key="AIzaSyCSjm9BHbo5hJIHf_Pe80cgisSGXpdVPCA")
model = genai.GenerativeModel("gemini-2.0-flash")

st.header("📚 Book Explainer")
uploader = st.file_uploader("Enter a file")
question = st.text_input("Ask your question")
voique = st.audio_input()
prompt = "I want answer for this question after reading all text"

if uploader:
    pdf = PdfReader(uploader)
    a = ""
    for i in range (len(pdf.pages)):
        a=a+ (pdf.pages[i].extract_text()) + " "
    responce = model.generate_content(a + prompt + question)
    if st.button("Click to get your answer"):
        st.write(responce.text)
