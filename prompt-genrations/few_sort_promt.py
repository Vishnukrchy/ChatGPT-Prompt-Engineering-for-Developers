import openai
from dotenv import load_dotenv
import os
import streamlit as st

# Load environment variables
load_dotenv()

# Configure OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE", "").rstrip("/")
openai.api_type = os.getenv("OPENAI_API_TYPE", "azure")  # Default to Azure
openai.api_version = os.getenv("OPENAI_API_VERSION")


def classify_sentiment(user_input):
    """Classify the sentiment of a given sentence using a few-shot prompt."""
    few_shot_prompt = f"""
    Classify the sentiment of the following sentences as "positive", "negative", or "neutral".

    Example 1:
    Sentence: "I absolutely love this product! It's amazing."
    Sentiment: positive

    Example 2:
    Sentence: "The service was terrible and the staff was rude."
    Sentiment: negative

    Example 3:
    Sentence: "I ordered a coffee and it was delivered on time."
    Sentiment: neutral

    Now, classify this sentence:
    Sentence: {user_input}
    Sentiment:"""

    try:
        response = openai.Completion.create(
            engine="shramin-gpt-35-turbo",  # Replace with your deployment name
            prompt=few_shot_prompt,
            max_tokens=10,  # Minimal tokens required for the sentiment
            temperature=0.0
        )
        return response.choices[0].text.strip()
    except openai.error.InvalidRequestError as e:
        return f"Error: Invalid request - {e}"
    except openai.error.APIError as e:
        return f"Error: API issue - {e}"
    except Exception as e:
        return f"Unexpected error: {e}"


def main():
    st.title("Sentiment Classifier")
    st.markdown("""
        This app uses a few-shot prompt to classify the sentiment of sentences as **positive**, **negative**, or **neutral**.
        Enter a sentence below to analyze its sentiment.
    """)

    user_input = st.text_area("Enter a sentence:", placeholder="Type a sentence to classify sentiment...", height=100)

    if st.button("Classify Sentiment"):
        if user_input.strip():
            with st.spinner("Classifying sentiment..."):
                sentiment = classify_sentiment(user_input)
            st.subheader("Sentiment")
            st.write(f"**{sentiment.capitalize()}**")
        else:
            st.error("Please enter a valid sentence to classify.")

if __name__ == "__main__":
    main()
