import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE", "").rstrip("/")  # Remove trailing slash
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")


def get_ai_response(prompt):
    response = openai.Completion.create(
        engine="shramin-gpt-35-turbo",  # Replace with your deployment name
        prompt=prompt,
        temperature=0.7,
        max_tokens=500  # Added to control response length
    )
    return response['choices'][0]['text'].strip()

# Example zero-shot prompt
prompt = "Generate a random number between 1 and 10"
response = get_ai_response(prompt)
print(response)