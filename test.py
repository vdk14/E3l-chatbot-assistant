import requests

url = "http://127.0.0.1:8000/chat/"
data = {
    "conversation_id": "12345",
    "user_input": "What is AI?"
}

response = requests.post(url, json=data)
print(response.json())  
