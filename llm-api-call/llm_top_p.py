from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

#Top P -> it is a value between 0 and 1 that controls the diversity of the generated text. and control the creativeness of the output. of response.

# The general recommendation is to alter temperature or Top P but not both.

top_p=input("enter the top p value: ")

google_api_key = os.getenv("GOOGLE_API_KEY")
llm=GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=google_api_key,
    top_p=top_p
)

result=llm.invoke("give me the meaning of life?")

print(result)
