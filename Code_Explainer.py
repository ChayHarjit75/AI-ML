import streamlit as st
import google.generativeai as genai
st.title("Code explainer")
genai.configure(api_key="AIzaSyCSjm9BHbo5hJIHf_Pe80cgisSGXpdVPCA")
model = genai.GenerativeModel("gemini-2.0-flash")
prompt1 = st.text_area(label="Provide your code")
prompt = """ Now you are a code explainer. Provide me the summary followed by line by line 
            explanation of the code."""
if prompt1:
    response = model.generate_content(prompt1+prompt)
    st.write(response.text)
