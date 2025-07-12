import streamlit as st
import openai
from chatbot import ask_bot
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Hospital Bot - BotMint", page_icon="🩺")
st.title("🩺 BotMint Hospital Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask something about the hospital:")

if user_input:
    bot_response = ask_bot(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("BotMint", bot_response))

for sender, msg in reversed(st.session_state.chat_history):
    st.markdown(f"**{sender}:** {msg}")
