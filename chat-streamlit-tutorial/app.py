import streamlit as st
import google.generativeai as genai
from functions import get_secret


 #genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.5-flash")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if not st.session_state.chat_history:
    st.session_state.chat_history.append(("assistant", "Hi! How can I help you?"))

user_message = st.chat_input("Type your message...")

if user_message:
    st.chat_message("user").write(user_message)
    st.session_state.chat_history.append(("user", user_message))

    system_prompt = f"""
    You are an assistant.
    Be nice and kind in all your responses.
    """
    full_input = f"{system_prompt}\n\nUser message:\n\"\"\"{user_message}\"\"\""

    response = model.generate_content(full_input)
    assistant_reply = response.text

    st.chat_message("assistant").write(assistant_reply)
    st.session_state.chat_history.append(("assistant", assistant_reply))