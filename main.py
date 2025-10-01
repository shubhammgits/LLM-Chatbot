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

