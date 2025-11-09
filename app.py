import streamlit as st
import google.generativeai as genai
from langdetect import detect


st.title("🌍 Multilingual Chatbot (Gemini API)")
st.markdown("This chatbot auto-detects your language and replies appropriately using Google Gemini.")


api_key = st.text_input("🔑 Enter your Google AI API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    
    if "history" not in st.session_state:
        st.session_state.history = []

   
    user_input = st.text_input("💬 Say something in any language:")

    if user_input:
        lang = detect(user_input)
        st.session_state.history.append(("You", user_input))

       
        prompt = f"Respond in the same language ({lang}) and in a culturally appropriate way: {user_input}"

        response = model.generate_content(prompt)
        reply = response.text.strip()

        st.session_state.history.append(("Bot", reply))


    for speaker, text in st.session_state.history:
        st.markdown(f"**{speaker}:** {text}")
