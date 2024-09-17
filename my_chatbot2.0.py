# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:27:21 2024

@author: Jiaqi Ye
"""

from transformers import pipeline
import streamlit as st
# import torch

# Check if CUDA (GPU) is available
# device = 0 if torch.cuda.is_available() else -1

# Define the chatbot function

'''
This chatbot is now powered by the facebook/blenderbot_small model, which is free...so not very clever.

'''

def chatbot(text):    
    responses = {
        "Who is Jiaqi?": "Jiaqi Ye is currently working as a Research Scientist, specializing in applied AI, data science, and robotic technologies. Check out his home page: https://bit.ly/JiaqiYe-HomePage for more details!"
    }
    return responses.get(text, None)

try:
    chatbot2 = pipeline(task="text2text-generation", model="facebook/blenderbot_small-90M")
except Exception as e:
    st.error(f"Failed to load the model: {e}")


def keyword_match(text):

    keywords = ["Jiaqi", "Jiaqi Ye"]

    for keyword in keywords:
        if keyword.lower() in text.lower():
            # Forward the request to the chatbot for a predefined response
            return chatbot("Who is Jiaqi?")  # Return a general response about Jiaqi
    return None

# Streamlit GUI
# def main():
#     st.title("My Silly Chatbot")

#     user_input = st.text_input("You: ", "")
#     if st.button("Send"):
#         if user_input:
#             response = chatbot2(user_input)
#             st.write("Chatbot: " + response[0]['generated_text'])
#         else:
#             st.write("Please enter a message.")
            
# Streamlit GUI
def main():
    st.title("My Silly Chatbot")

    # Initialize session state for chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Text input for user messages
    user_input = st.text_input("Message to Jiaqi's chatbot': ", "")

    if st.button("Send") and user_input:
        # Cache the response to minimize repeated computation
        @st.cache_data(show_spinner=False)
        def get_model_response(text):
            return chatbot2(text)[0]['generated_text'] 
        # Generate response
        user_response = keyword_match(user_input)

        if user_response:
            response = user_response
        else:
            response = get_model_response(user_input)

        # Append the user input and response to the chat history
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("chatbot", response))

    # # Debugging: Print chat history to verify its structure
    # st.write("Chat history (debug):", st.session_state.chat_history)

    # Display chat history with alignment
    for role, message in st.session_state.chat_history:
        if role == "user":
            with st.container():
                cols = st.columns([3, 1])  # Adjust column widths if needed
                with cols[1]:  # Right side for user
                    st.write(f"**You:** {message}", align="right")
                with cols[0]:  # Left side for chatbot
                    st.empty()  # Empty space for alignment
        elif role == "chatbot":
            with st.container():
                cols = st.columns([2, 2])  # Adjust column widths if needed
                with cols[0]:  # Left side for chatbot
                    st.write(f"**Chatbot:** {message}")
                with cols[1]:  # Right side for user
                    st.empty()  # Empty space for alignment
        else:
            st.write("Invalid chat history entry:", (role, message))


if __name__ == "__main__":
    main()
