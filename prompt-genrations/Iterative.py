import openai
from dotenv import load_dotenv
import os

from pyexpat.errors import messages

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE", "").rstrip("/")  # Remove trailing slash
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")

def get_ai_response(prompt):
    messages =[{"role":"user","content":prompt}]
    response = openai.ChatCompletion.create(
        engine="shramin-gpt-35-turbo",  # Replace with your deployment name
        messages=messages,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']

'''
Iterative prompt Development
ll iteratively analyze and refine your prompts to generate better results.
'''

# Generate a marketing product description from a product fact sheet

fact_sheet_chair="""
Oversview
- Part of a beautiful family of mid-century inspired office furniture, 
including filing cabinets, desks, bookshelves, meeting tables, and more.
- Several options available in memory finish around white or black, 
with glass top or wood top.
- Available in L, W, and H options.
- Available with plastic back and front or full leather top.
- Multiple options of square or rectangular top.
- Available in metal, glass, or wood.
- Suitable for home or business settings.

CONSTRUCTION
- 5-year limited warranty provided in the US.
- Legs: Steel.
- Top: Glass or Leather.
- Wood: Janka rating of 1000 or higher.

SIZE
- S: 28" x 34" x 20"
- M: 31" x 39" x 25"
- L: 34" x 40" x 28"

OPTIONS
- Soft or hard-floor caster options.
- Two choices of seat foam densities: 
  - Medium (17lb)
  - High (20lb)
- Two choices of interior wall mount options:
  - Wood
  - Steel

COLORS
- Spacegrey
- Black
- Beige
- Walnut
- Grey
- Black

MATERIALS
- Solid Wood: Janka rating of 1000 or higher
- Leather: Viscose fibres
- Glass: UV resistant with UV blocker
CAPACITY
- Single person
- Double person

COUNTRY OF ORIGIN
- INDIA
"""

prompt=f""" Your Task is help the marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the following information:

Target audience: Furniture retailers
Focus: Technical aspects and materials
Word limit: 50 words
Additionally, provide the following information in JSON format:

name
color
type
summary
Technical specifications: ```{fact_sheet_chair}```"""

# response=get_ai_response(prompt)
# print("AI Response -: "+response)


prompt2 = f"""
Your task is to help a marketing team create a description for a retail website of a product based on a technical fact sheet.

Write a product description based on the information provided in the technical specifications delimited by triple backticks.

The description is intended for furniture retailers, so should be technical in nature and focus on the materials the product is constructed from.

At the end of the description, include every 7-character Product ID in the technical specification.

After the description, include a table that gives the product's dimensions. The table should have two columns.In the first column include the name of the dimension. 
In the second column include the measurements in inches only.

Give the table the title 'Product Dimensions'.

Format everything as HTML that can be used in a website. Place the description in a <div> element.

Technical specifications: ```{fact_sheet_chair}```
"""
print(get_ai_response(prompt2))

