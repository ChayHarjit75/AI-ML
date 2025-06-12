import streamlit as st
from gtts import gTTS
from googletrans import LANGUAGES
from googletrans import Translator
trans = Translator()
st.header("Hi, Welcome to Translation Site")
langu = st.text_input("Enter the Language you want to Translate: ")
tex = st.text_input("Enter the Text you want to the Language: ")
d = {}
for code, name in LANGUAGES.items():
    d[name] = code
    if langu and tex:
        t = trans.translate(tex, dest= d[langu.lower()])
        tts = gTTS(t.text, lang=d[langu.lower()])
        tts.save("translate.mp3")
        st.audio("translate.mp3")
        st.write(t.text)
