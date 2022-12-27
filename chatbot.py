import requests

def send_message(message):
    api_key = "YOUR_API_KEY"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {"model": "text-davinci-003",
  "prompt": message}
    response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=data)
    response_text = response.json()['choices'][0]['text']
    return response_text

while True:
    message = input("You: ")
    response = send_message(message)
    print(f"Assistant: {response}")
