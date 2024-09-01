# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:05:23 2024

@author: Jiaqi Ye
"""
# import openai
# from transformers import pipeline
import streamlit as st

# Define the chatbot function
def chatbot(text):
    responses = {
        "Hi": "Hello!",
        "How are you?": "I am fine, thanks! How are you?",
    }
    # Return the response if it's in the predefined responses, else default message
    return responses.get(text, "Sorry, I don't understand that.")

# Streamlit GUI
def main():
    st.title("My Silly Chatbot")

    user_input = st.text_input("You: ", "")
    if st.button("Send"):
        if user_input:
            response = chatbot(user_input)
            st.write("Chatbot: " + response)
        else:
            st.write("Please enter a message.")

if __name__ == "__main__":
    main()