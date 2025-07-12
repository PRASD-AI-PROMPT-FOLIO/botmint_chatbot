import pandas as pd
import csv
import streamlit as st
from chatbot import ask_bot

# Set page title and icon
st.set_page_config(page_title="Hospital Bot - BotMint", page_icon="🩺")
st.image("logo.png", width=150)
st.title("🩺 BotMint Hospital Chatbot")

# ✅ Initialize chat history before any interaction
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Quick reply buttons
st.markdown("### 🧭 Quick Questions")
col1, col2 = st.columns(2)

with col1:
    if st.button("🏥 Departments"):
        st.session_state.chat_history.append({"role": "user", "content": "What departments are available?"})
        response = ask_bot("What departments are available?")
        st.session_state.chat_history.append({"role": "assistant", "content": response})

    if st.button("👨‍⚕️ Doctors"):
        st.session_state.chat_history.append({"role": "user", "content": "List all doctors"})
        response = ask_bot("List all doctors")
        st.session_state.chat_history.append({"role": "assistant", "content": response})

with col2:
    if st.button("⏰ Opening Hours"):
        st.session_state.chat_history.append({"role": "user", "content": "What are the opening hours?"})
        response = ask_bot("What are the opening hours?")
        st.session_state.chat_history.append({"role": "assistant", "content": response})

    if st.button("📍 Location"):
        st.session_state.chat_history.append({"role": "user", "content": "Where is the hospital located?"})
        response = ask_bot("Where is the hospital located?")
        st.session_state.chat_history.append({"role": "assistant", "content": response})

# Chat input field
user_input = st.chat_input("Ask something about the hospital:")
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    response = ask_bot(user_input)
    st.session_state.chat_history.append({"role": "assistant", "content": response})

# Chat history display
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Google Form (optional)
st.markdown("---")
st.markdown("📎 [Fill out our feedback form (with file upload)](https://forms.gle/YOUR_PUBLIC_FORM_LINK)")

# Export to CSV
chat_data = pd.DataFrame(st.session_state.chat_history)
csv = chat_data.to_csv(index=False).encode('utf-8')
st.download_button(
    label="💾 Download Chat as CSV",
    data=csv,
    file_name='chat_history.csv',
    mime='text/csv',
)

