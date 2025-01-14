import openai
from click import prompt
from  dotenv import load_dotenv
import  os

from pyexpat.errors import messages

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE", "").rstrip("/")  # Remove trailing slash
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")


def get_ai_response(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        engine="shramin-gpt-35-turbo",  # Replace with your deployment name
        messages=messages,
        temperature=0
    )
    return response.choices[0].message["content"]



def get_chat_response(prompt):
    response = get_ai_response(prompt)
    return response

prompt=f"""
Your task is to answer in a concise and professional .
You are a helpful assistant that translates English.
"""

while True:
    user_input = input("User: ")
    response = get_chat_response(user_input)
    print("Assistant:", response)