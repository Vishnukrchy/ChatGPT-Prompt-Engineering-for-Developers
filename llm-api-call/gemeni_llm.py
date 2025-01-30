from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=google_api_key
)

result = llm.invoke("What is the capital of India?")

print(result)