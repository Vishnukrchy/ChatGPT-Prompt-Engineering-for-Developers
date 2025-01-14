import openai
from  dotenv import load_dotenv
import  os
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE", "").rstrip("/")  # Remove trailing slash
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")


def get_ai_response(prompt):
    """
    Fetches a response from the OpenAI ChatCompletion API using the given prompt.

    Args:
        prompt (str): The user's input for the AI.

    Returns:
        str: The AI's response, or None if an error occurs.
    """
    try:
        #Ensure required environment variables are set
        if not openai.api_key or not openai.api_base or not openai.api_version:
            raise ValueError("Missing required environment variables for OpenAI configuration.")
        #send request to OpenAI
        response =openai.ChatCompletion.create(
            engine="shramin-gpt-35-turbo", #replace with your deployment name or model name
            #massage is set of instruction and input
            messages=[
                {"role":"user" ,"content":prompt}
            ]
            ,
            temperature=0 #this is the degree of randomness of the model's output
        )
        #extract the AI response from the API response
        # return response['choices'][0]['message']['content']
        return  response.choices[0].message["content"]
    except openai.error.AuthenticationError as e:
        print(f"Authentication Error: {e}")
    except openai.error.OpenAIError as e:
        print(f"OpenAI API Error: {e}")


text = """give me an example of a good book"""

"""
    =================Prompting Principles =====================
Principle 1: Write clear and specific instructions
Principle 2: Give the model time to “think”
Tactics
Tactic 1: Use delimiters to clearly indicate distinct parts of the input
Delimiters can be anything like: ```, \`, etc.
Tactic 2: Use a prompt to guide the model’s thinking process
"""
text = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""

prompt_1 = f"""
Summarize the following text delimited by triple backticks with 1 sentence.

```{text}```
"""

print("prompt 1 AI response: " +get_ai_response(prompt_1))

