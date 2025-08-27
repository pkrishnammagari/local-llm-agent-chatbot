import requests
import json

url = "http://localhost:11434/api/chat"

#The data we are sending to the API
my_data = {
    "model": "llama3",
    "stream": False,
    "messages": [
        {"role": "user", "content": "Hello, how are you?"}
    ]
}

#Sending a post request to the API
response = requests.post(url, json=my_data)

response_data = response.json()
message_content = response_data['message']['content']

print("Response from API:", message_content)