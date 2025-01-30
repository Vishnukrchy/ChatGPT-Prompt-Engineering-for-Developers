"""
Prompt Elements ->A prompt contains any of the following elements:

Prompt Templates-> Prompt Templates is a way to structure your prompts to make them more readable and easier to use.
Prompt Variables -> Prompt Variables are variables that you can use in your prompts.
Prompt Delimiters -> Prompt Delimiters are characters that are used to delimit your prompts.
Prompt Functions  -> Prompt Functions are functions that you can use in your prompts.
  
  
Instruction - a specific task or instruction you want the model to perform
Context - external information or additional context that can steer the model to better responses
Input Data - the input or question that we are interested to find a response for
Output Data - the output or result that we want the model to generate
"""
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Initialize the Google Generative AI model
llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",  # Specify the model you want to use
    google_api_key=os.getenv("GOOGLE_API_KEY")  # Get the API key from environment variables
)

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
    response = llm.invoke(prompt)  # Send the prompt to the AI model
    print("\nHere's your answer:")
    print(response)  # Display the AI's response
except Exception as e:
    print(f"Oops! Something went wrong: {e}")  # Handle errors gracefully