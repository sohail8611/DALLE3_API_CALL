import requests
import json
import os
import os
# Replace with your OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Define the API endpoint and request payload
api_url = 'https://api.openai.com/v1/images/generations'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}
data = {
    "model": "dall-e-3",
    "prompt": "a white siamese cat",
    "n": 1,
    "size": "1024x1024"
}

# Make the API request
response = requests.post(api_url, headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 200:
    result = response.json()
    print("Generated image URL:", result['data'][0]['url'])
else:
    print("Error:", response.status_code, response.text)
