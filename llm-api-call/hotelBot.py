from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define the role and context for the AI
role = "You are a friendly virtual assistant for Sunshine Hotel."
context = (
    "Sunshine Hotel offers amazing amenities like a swimming pool, free Wi-Fi, "
    "a fitness center, and an in-house restaurant. Here are some additional details:\n"
    "- Check-in time: 2:00 PM\n"
    "- Check-out time: 11:00 AM\n"
    "- Address: 123 Beachside Lane, Miami, FL\n"
    "- Contact: +1-800-555-6789"
)

# Ask the user for their question
print("Welcome to Sunshine Hotel! How can I assist you today?")
user_question = input("Please enter your question: ")

# Combine the role, context, and user's question into a single prompt
prompt = f"{role}\n\n{context}\n\nUser's Question: {user_question}"

# Get the AI's response
try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Use GPT-3.5-turbo or any other OpenAI model
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": prompt}
        ]
    )
    # Extract and display the AI's response
    ai_response = response.choices[0].message.content
    print("\nHere's your answer:")
    print(ai_response)
except Exception as e:
    print(f"Oops! Something went wrong: {e}")  # Handle errors gracefully