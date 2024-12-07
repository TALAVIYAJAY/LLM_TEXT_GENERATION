import requests
from django.shortcuts import render
from dotenv import load_dotenv  # Import the load_dotenv function
import os

# Load environment variables from .env file
load_dotenv()

# Your Hugging Face API Key
API_KEY = os.getenv("HUGGINGFACE_API_KEY")  # Get the API key from the environment variable

# Hugging Face API URL for GPT-J 6B (use the desired model here)
API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B"

# Set up headers for authentication
headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def ask_huggingface_api(question):
    data = {
        "inputs": question
    }

    # Send the POST request to Hugging Face API
    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        model_response = response.json()[0]['generated_text']

        # Clean the response to remove the question and unwanted parts
        cleaned_response = " ".join(model_response.split())  # Join words into a single line with proper spacing
        
        # Remove the question part (if the model includes the question in the response)
        if cleaned_response.lower().startswith(question.lower()):
            cleaned_response = cleaned_response[len(question):].strip()

        # Remove incomplete sentence at the end
        if cleaned_response.endswith(','):
            cleaned_response = cleaned_response.rsplit(',', 1)[0]
        
        # Ensure the response ends with proper punctuation
        if not cleaned_response.endswith(('.', '?', '!')):
            cleaned_response += '.'

        return cleaned_response
    else:
        return f"Error: {response.status_code}, {response.text}"

# Ask question view
def ask_question(request):
    response_data = None

    if request.method == 'POST':
        user_question = request.POST.get('question')  # Get the question from the form
        
        if user_question:
            # Call Hugging Face API to get the response for the user's question
            response_data = ask_huggingface_api(user_question)

    return render(request, 'ask_question.html', {'response': response_data})
