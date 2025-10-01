import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

st.set_page_config(
    page_title="Chat with Gemini",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto"
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest')


def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role
    

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("🤖 Chat with Gemini")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

