
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os


# max tokens -> it is the maximum number of tokens that the model can generate in a single response.
# Load environment variables from .env
# nv file
load_dotenv()
# Check if the Google API key is set
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set.")

# Initialize the Google Generative AI model
llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=google_api_key,
    max_output_tokens=1024,
    max_input_tokens=2048,
)
prompt =input("""Enter your prompt: """)

result = llm.invoke(prompt)

print("Result:", result)