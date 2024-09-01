# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:52:22 2024

@author: Jiaqi Ye
"""

from transformers import pipeline

# Initialize the conversational pipeline with the BlenderBot model
chatbot = pipeline(task="text2text-generation", model="facebook/blenderbot-400M-distill")

# Start chatting with the bot
print("Start chatting with the bot (type 'exit' to stop)...")

# Keep track of the conversation history within the pipeline itself
while True:
    user_message = input("You: ")
    
    # Exit condition
    if user_message.lower() == "exit":
        break

    # Pass the user message to the chatbot pipeline
    response = chatbot(user_message)

    # Print the bot's reply
    print("Bot:", response[0]['generated_text'])
