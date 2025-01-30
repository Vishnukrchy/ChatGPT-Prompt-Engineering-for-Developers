from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

#Temperature -> it is a value between 0 and 2 that controls the randomness of the generated text. and control the creativeness of the output. of response.

temprature=input("enter the temprature value: ")

google_api_key = os.getenv("GOOGLE_API_KEY")
llm=GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=google_api_key,
    temprature=temprature
)

result=llm.invoke("Hello What is GenAI?")

print(result)