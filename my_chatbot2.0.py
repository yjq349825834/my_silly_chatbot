# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:27:21 2024

@author: Jiaqi Ye
"""

import requests

# Replace with your own API key
API_KEY = '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'
MODEL_NAME = 'distilbert-base-uncased'  # You can replace this with any model you want to use
API_URL = f'https://api-inference.huggingface.co/models/{MODEL_NAME}'

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raises an HTTPError if the response code was unsuccessful
        return response.json()
    except requests.exceptions.HTTPError as err:
        return {"error": str(err)}
    except Exception as e:
        return {"error": str(e)}

# Example usage
prompt = "Hello, how are you?"
payload = {"inputs": prompt}
result = query(payload)
print(result)
