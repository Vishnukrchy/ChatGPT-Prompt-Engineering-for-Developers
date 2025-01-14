import os
from dotenv import load_dotenv
import openai

# Load the environment variables from the .env file
load_dotenv()

# Configure OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE", "").rstrip("/")  # Remove trailing slash
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")


# def get_completion(prompt, model="gpt-3.5-turbo"):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0, # this is the degree of randomness of the model's output
#     )
#     return response.choices[0].message["content"]

# def get_chat_response(prompt):
def get_ai_response(prompt):
    """
    Fetches a response from the OpenAI ChatCompletion API using the given prompt.

    Args:
        prompt (str): The user's input for the AI.

    Returns:
        str: The AI's response, or None if an error occurs.
    """
    try:
        # Ensure required environment variables are set
        if not openai.api_key or not openai.api_base or not openai.api_version:
            raise ValueError("Missing required environment variables for OpenAI configuration.")

        # Send request to OpenAI
        response = openai.ChatCompletion.create(
            engine="shramin-gpt-35-turbo",  # Replace with your deployment name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )
        # Extract the AI response from the API response
        return response['choices'][0]['message']['content']
    except openai.error.AuthenticationError as e:
        print(f"Authentication Error: {e}")
    except openai.error.OpenAIError as e:
        print(f"OpenAI API Error: {e}")
    except ValueError as e:
        print(f"Configuration Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    return None


# sample prompt for testing

text = r"""
In a charming village, siblings Jack and Jill set out on \
a quest to fetch water from a hilltop \
well. As they climbed, singing joyfully, misfortune \
struck—Jack tripped on a stone and tumbled \
down the hill, with Jill following suit. \
Though slightly battered, the pair returned home to \
comforting embraces. Despite the mishap, \
their adventurous spirits remained undimmed, and they \
continued exploring with delight.
"""
# example 1
prompt_1 = f"""
Perform the following actions: 
1 - Summarize the following text delimited by triple \
backticks with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the following \
keys: french_summary, num_names.

Separate your answers with line breaks.

Text:
```{text}```
"""


prompt = f"""
Generate a list of three made-up book titles along \ 
with their authors and genres. 
Provide them in JSON format with the following keys: 
book_id, title, author, genre.
"""

# Get AI response for the sample prompt
# response = get_ai_response(prompt_1)
response = get_ai_response(prompt)
if response:
    print("AI Response:", response)
else:
    print("Failed to generate a response.")

