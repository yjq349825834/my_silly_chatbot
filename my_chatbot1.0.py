# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:05:23 2024

@author: Jiaqi Ye
"""

from transformers import pipeline

import streamlit as st

# # Load a pre-trained model
# chatbot = pipeline('question-answering', model='facebook/blenderbot-3B')


def chatbot(text):
    if text == "Hi":
        response = "Hello"
    if text == "How are you?":
        response = "I am fine, thanks, how are you?"
    return response

def get_chatbot_response(text):
    response = chatbot(text)
    return response

        
# Streamlit GUI
def main():
    st.title("My Silly Chatbot")

    user_input = st.text_input("You: ", "Hello!")
    if st.button("Send"):
        response = chatbot(user_input)
        st.write("Chatbot: " + response)

if __name__ == "__main__":
    main()
