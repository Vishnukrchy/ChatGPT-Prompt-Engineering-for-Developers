import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE", "").rstrip("/")  # Remove trailing slash
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")


def get_ai_response(prompt):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        engine="shramin-gpt-35-turbo",  # Replace with your deployment name
        messages=messages,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']


# Chain-of-Thought (CoT) prompt
cot_prompt = """
Solve the following problem step by step. Take your time to think carefully and show your work.

Problem: {problem}

Step 1: Understand the problem.
- Read the problem carefully.
- Identify what is given and what is being asked.
- Break the problem into smaller, manageable parts.

Step 2: Plan the solution.
- Think about the approach you will use to solve the problem.
- Write down the formulas, methods, or strategies you will apply.
- Consider any assumptions or constraints.

Step 3: Execute the plan.
- Perform the calculations or steps one by one.
- Show all intermediate results and explain your reasoning.

Step 4: Verify the solution.
- Double-check your calculations and logic.
- Ensure the final answer makes sense in the context of the problem.
- Reflect on whether there are alternative solutions or improvements.

Final Answer: {final_answer}
"""

# Example usage
problem = """
A bakery operates in a busy city. In the morning, they sell 15 cupcakes, 20 cookies, and 10 muffins. 
In the afternoon, they sell 25 cupcakes, 30 cookies, and 15 muffins. Each cupcake costs $2, each cookie costs $1, and each muffin costs $3. 
Additionally, the bakery has fixed daily costs of $100 for rent, utilities, and staff salaries.

1. Calculate the total revenue from cupcakes, cookies, and muffins separately.
2. Calculate the total revenue for the day.
3. Calculate the bakery's profit for the day after deducting fixed costs.
4. If the bakery wants to increase its daily profit by 20%, how much additional revenue does it need to generate?
"""

solution = """
Step 1: Understand the problem.
- Given:
  - Morning sales:
    - Cupcakes: 15
    - Cookies: 20
    - Muffins: 10
  - Afternoon sales:
    - Cupcakes: 25
    - Cookies: 30
    - Muffins: 15
  - Prices:
    - Cupcake: $2
    - Cookie: $1
    - Muffin: $3
  - Fixed daily costs: $100
- Asked:
  1. Total revenue from cupcakes, cookies, and muffins separately.
  2. Total revenue for the day.
  3. Profit for the day after deducting fixed costs.
  4. Additional revenue needed to increase daily profit by 20%.

Step 2: Plan the solution.
- Calculate the total number of each item sold (morning + afternoon).
- Calculate the revenue for each item type (total items sold * price per item).
- Sum the revenues to get the total revenue for the day.
- Subtract fixed costs from total revenue to get the profit.
- Calculate 20% of the current profit to determine the additional revenue needed.

Step 3: Execute the plan.
1. Total items sold:
   - Cupcakes: 15 (morning) + 25 (afternoon) = 40
   - Cookies: 20 (morning) + 30 (afternoon) = 50
   - Muffins: 10 (morning) + 15 (afternoon) = 25

2. Revenue by item type:
   - Cupcakes: 40 * $2 = $80
   - Cookies: 50 * $1 = $50
   - Muffins: 25 * $3 = $75

3. Total revenue for the day:
   - Total revenue = $80 (cupcakes) + $50 (cookies) + $75 (muffins) = $205

4. Profit for the day:
   - Profit = Total revenue - Fixed costs
   - Profit = $205 - $100 = $105

5. Additional revenue needed for 20% profit increase:
   - 20% of current profit = 0.20 * $105 = $21
   - Additional revenue needed = $21

Step 4: Verify the solution.
- The calculations are correct.
- The final answers are reasonable for the given problem.

Final Answer:
1. Revenue from cupcakes: $80, cookies: $50, muffins: $75.
2. Total revenue for the day: $205.
3. Profit for the day: $105.
4. Additional revenue needed to increase profit by 20%: $21.
"""

# Format the prompt with the problem and solution
formatted_prompt = cot_prompt.format(
    problem=problem,
    final_answer="""
1. Revenue from cupcakes: $80, cookies: $50, muffins: $75.
2. Total revenue for the day: $205.
3. Profit for the day: $105.
4. Additional revenue needed to increase profit by 20%: $21.
"""
)
print(formatted_prompt)