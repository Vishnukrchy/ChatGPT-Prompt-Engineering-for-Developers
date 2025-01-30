from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Check if the Google API key is set
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set.")

# Initialize the Google Generative AI model
llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=google_api_key
)

# Define a prompt template (optional, if you want structured input)
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="Answer the following question: {question}"
)

# Get user input
question = input("Enter your prompt: ")

# Format the prompt using the template (if using PromptTemplate)
formatted_prompt = prompt_template.format(question=question)

# Stream the response from the model
# here in stream we are printing the response as it arrives
try:
    for chunk in llm.stream(formatted_prompt):
        print(chunk, end="", flush=True)  # Print chunks as they arrive
except Exception as e:
    print(f"An error occurred: {e}")