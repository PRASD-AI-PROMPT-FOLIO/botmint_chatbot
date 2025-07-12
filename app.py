import streamlit as st
from chatbot import ask_bot

st.set_page_config(page_title="Hospital Bot - BotMint", page_icon="🩺")
st.image("logo.png", width=150)  # you can adjust width if needed
st.title("🩺 BotMint Hospital Chatbot")
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
