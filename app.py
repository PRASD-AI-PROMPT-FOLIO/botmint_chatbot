import streamlit as st
from chatbot import ask_bot

st.set_page_config(page_title="Hospital Bot - BotMint", page_icon="🩺")
st.title("🩺 BotMint Hospital Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask something about the hospital:")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    response = ask_bot(user_input)
    st.session_state.chat_history.append({"role": "assistant", "content": response})

# Display chat history using nice formatting
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Optional: link to Google Form
st.markdown("---")
st.markdown("📎 [Fill out our feedback form (with file upload)](https://forms.gle/YOUR_PUBLIC_FORM_LINK)")
