import openai
from dotenv import load_dotenv
import os
import streamlit as st  # Import Streamlit for the app

# Load environment variables
load_dotenv()

# Configure OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE", "").rstrip("/")
openai.api_type = os.getenv("OPENAI_API_TYPE", "azure")  # Default to Azure
openai.api_version = os.getenv("OPENAI_API_VERSION")


def get_llm_response(prompt):
    """Fetch a response from the LLM with proper error handling."""
    try:
        response = openai.ChatCompletion.create(
            engine="shramin-gpt-35-turbo",  # Replace with your deployment name
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        return response['choices'][0]['message']['content'].strip()
    except openai.error.InvalidRequestError as e:
        return f"Error: Invalid request - {e}"
    except openai.error.APIError as e:
        return f"Error: API issue - {e}"
    except Exception as e:
        return f"Unexpected error: {e}"


def main():
    st.title("AI Math Problem Solver with Meta-Prompting")
    st.markdown("""
        This app demonstrates meta-prompting to generate a better prompt for solving math word problems. 
        Enter a problem to generate a solution step-by-step.
    """)

    # Step 1: Meta-Prompting to generate a better prompt
    meta_prompt = """
    Your task is to create a better prompt for solving math word problems. The prompt should guide the model to break down the problem into clear, logical steps and provide the final answer.

    Write a prompt that would help the model solve this problem step by step. Be clear and concise.
    """

    if st.button("Generate Improved Prompt"):
        with st.spinner("Generating improved prompt..."):
            generated_prompt = get_llm_response(meta_prompt)
        st.subheader("Generated Prompt")
        st.text_area("Improved Prompt", value=generated_prompt, height=200)

        # Step 2: Use the generated prompt to solve a math problem
        problem = st.text_area("Enter a math problem to solve:", placeholder="E.g., Sarah has 15 apples. She gives 4 to her friend and buys 10 more. How many does she have now?")

        if st.button("Solve Problem"):
            if problem.strip():
                final_prompt = f"{generated_prompt}\n\nProblem: {problem}"
                with st.spinner("Solving the problem..."):
                    solution = get_llm_response(final_prompt)
                st.subheader("Solution")
                st.markdown(solution)
            else:
                st.error("Please enter a valid math problem to solve.")


if __name__ == "__main__":
    main()
