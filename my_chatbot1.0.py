# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:05:23 2024

@author: Jiaqi Ye
"""
# import openai
from transformers import pipeline
import streamlit as st
import torch

# Check if CUDA (GPU) is available
device = 0 if torch.cuda.is_available() else -1

# Define the chatbot function

'''
Need to replace this with a proper LLM API, like GPT4.0, DistilBERT, facebook/blenderbot-small.

'''

def chatbot(text):    
    responses = {
        "Hi": "Hello!",
        "How are you?": "I am fine, thanks! How are you?",
    }
    # Return the response if it's in the predefined responses, else default message
    return responses.get(text, "Sorry, I don't understand that.")

chatbot2 = pipeline(task="text2text-generation", model="facebook/blenderbot-400M-distill", device=device,
                    torch_dtype=torch.float16 if device == 0 else None)


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
        def get_response(text, bot="chatbot2"):
            if bot == "chatbot2":    
                return chatbot2(text)[0]['generated_text'] 
            elif bot == "chatbot":
                return chatbot(text)
        # Generate response
        response = get_response(user_input, bot="chatbot2")

        # Append the user input and response to the chat history
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("chatbot", response))

    # Debugging: Print chat history to verify its structure
    st.write("Chat history (debug):", st.session_state.chat_history)

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