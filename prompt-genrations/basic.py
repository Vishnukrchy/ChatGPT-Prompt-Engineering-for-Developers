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
        # openai provides functionality for interacting with the OpenAI API that you can use to generate text, images, audio, and video.
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

# print("prompt 1 AI response: " +get_ai_response(prompt_1))

#1st Principle (Tactic — 02 Example) — Structured Output =========================
prompt_2= f"""
Genrate a list of three ai-ml book titles along \
with their authors and genres.
provide them in JSON format with the following keys: \
book_id, title, author, genre.
"""

#print("prompt 2 AI response: " +get_ai_response(prompt_2))
'''
output can expect
prompt 2 AI response: {
  "books": [
    {
      "book_id": 1,
      "title": "Artificial Intelligence: A Modern Approach",
      "author": "Stuart Russell, Peter Norvig",
      "genre": "Artificial Intelligence"
    },
    {
      "book_id": 2,
      "title": "Machine Learning: A Probabilistic Perspective",
      "author": "Kevin P. Murphy",
      "genre": "Machine Learning"
    },
    {
      "book_id": 3,
      "title": "Deep Learning",
      "author": "Ian Goodfellow, Yoshua Bengio, Aaron Courville",
      "genre": "Deep Learning"
    }
  ]
}
'''

#Tactic 3: Ask the model to check whether conditions are satisfied
# here text is an  example of  structured  sequence of instructions
text = f"""
make a cup of tea is easier than make a cup of coffee,
you need  get some \
water first. and  put the tea bag in the cup. \
ones the water is hot, \
put the tea bag in the cup and \
let it sit for a bit so the \
tea can brew. After a few seconds, \
turn off the heat so the \
tea can steep. After a few minutes, \
take out the tea bag. If you \
like, you can add some \
sugar or milk in the cup \
before taking the tea out.
"""

prompt_3 = f"""
you will be provided with text delimited by triple quotes. 
If it contains a sequence of instructions, \ 
re-write those instructions in the following format:

Step 1 - ...
Step 2 - ...
...
Step N - ...

if the text does not contain a sequence of instructions, \
then simply write \"No steps provided.\"

\"\"\"{text}\"\"\"
"""

# ai_response= get_ai_response(prompt_3)
# print(ai_response)
'''
Step 1 - Get some water.
Step 2 - Put the tea bag in the cup.
Step 3 - Heat the water until it is hot.
Step 4 - Put the tea bag in the cup and let it sit for a bit.
Step 5 - Turn off the heat.
Step 6 - Let the tea steep for a few minutes.
Step 7 - Take out the tea bag.
Step 8 - Optional: Add sugar or milk to the cup before taking the tea out.

'''

# Tactic 4: Use a prompt to guide the model’s thinking process
# here text is an  example of  not structured  sequence of instructions
text_2 = f"""
The sun is shining brightly today, and the birds are \
singing. It's a beautiful day to go for a \ 
walk in the park. The flowers are blooming, and the \ 
trees are swaying gently in the breeze. People \ 
are out and about, enjoying the lovely weather. \ 
Some are having picnics, while others are playing \ 
games or simply relaxing on the grass. It's a \ 
perfect day to spend time outdoors and appreciate the \ 
beauty of nature.
"""

prompt_4 = f"""
you will be provided with text delimited by triple quotes.
if it contains a sequence of instructions, \
re-write those instructions in the following format:

Step 1 - ...
Step 2 - ...
...
Step N - ...

if the text does not contain a sequence of instructions, \
then simply write \"No steps provided.\"

\"\"\"{text_2}\"\"\"
"""

ai_response= get_ai_response(prompt_4)
print(ai_response)
'''
No steps provided.
'''








