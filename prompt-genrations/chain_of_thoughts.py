import openai
from dotenv import load_dotenv
import os
import streamlit as st  # Added missing Streamlit import

# Load environment variables first
load_dotenv()

# Configure OpenAI API with proper error handling
if not all([os.getenv("OPENAI_API_KEY"), os.getenv("OPENAI_API_BASE"), os.getenv("OPENAI_API_VERSION")]):
    raise ValueError("Missing required OpenAI environment variables")

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE", "").rstrip("/")
openai.api_type = os.getenv("OPENAI_API_TYPE", "azure")  # Default to Azure
openai.api_version = os.getenv("OPENAI_API_VERSION")


def get_ai_response(prompt):
    """Get AI response with proper error handling"""
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    try:
        response = openai.ChatCompletion.create(
            engine="shramin-gpt-35-turbo",  # Azure deployment name
            messages=messages,
            temperature=0.7,
            max_tokens=500  # Added to limit response length
        )
        return response['choices'][0]['message']['content'].strip()

    except openai.error.InvalidRequestError as e:
        return f"Error: Invalid request - {e}"
    except openai.error.APIError as e:
        return f"Error: API issue - {e}"
    except Exception as e:
        return f"Unexpected error: {e}"


# Chain-of-Thought prompt template
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


# Example problem setup
def main():
    st.title("AI Problem Solver")

    problem = st.text_area("Enter your problem:", height=200, value="""A bakery operates in a busy city. In the morning, they sell 15 cupcakes, 20 cookies, and 10 muffins. 
In the afternoon, they sell 25 cupcakes, 30 cookies, and 15 muffins. Each cupcake costs $2, each cookie costs $1, and each muffin costs $3. 
Additionally, the bakery has fixed daily costs of $100 for rent, utilities, and staff salaries.

1. Calculate the total revenue from cupcakes, cookies, and muffins separately.
2. Calculate the total revenue for the day.
3. Calculate the bakery's profit for the day after deducting fixed costs.
4. If the bakery wants to increase its daily profit by 20%, how much additional revenue does it need to generate?""")

    if st.button("Solve"):
        formatted_prompt = cot_prompt.format(
            problem=problem,
            final_answer="""1. Revenue from cupcakes: $80, cookies: $50, muffins: $75.
2. Total revenue for the day: $205.
3. Profit for the day: $105.
4. Additional revenue needed to increase profit by 20%: $21."""
        )

        with st.spinner("Analyzing problem..."):
            solution = get_ai_response(formatted_prompt)

        st.subheader("Solution")
        st.markdown(solution)


if __name__ == "__main__":
    main()