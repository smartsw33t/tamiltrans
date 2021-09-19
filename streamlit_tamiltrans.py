from google_trans_new import google_translator
import streamlit as st
translator = google_translator()
st.title("மொழிபெயர்ப்புக் கருவி ")
text = st.text_input("ஆங்கிலத்தில் டைப் செய்யுங்கள்")
translate = translator.translate(text, lang_tgt='ta')
st.write(translate)
