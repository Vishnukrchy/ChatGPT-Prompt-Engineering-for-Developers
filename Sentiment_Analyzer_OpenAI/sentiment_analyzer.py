import openai
from dotenv import load_dotenv
import os
import streamlit as st

# Load environment variables
load_dotenv()

# Configure OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE", "").rstrip("/")  # Remove trailing slash
openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")

def get_sentiment(text):
    try:
        # Validate OpenAI configuration
        if not openai.api_key or not openai.api_base or not openai.api_version:
            raise ValueError("Missing required environment variables for OpenAI configuration.")

        # Call OpenAI API for sentiment analysis
        response = openai.ChatCompletion.create(
            engine="shramin-gpt-35-turbo",  # Replace with your deployment name
            messages=[
                {"role": "system", "content": "You are a sentiment analyzer. You will analyze the text given to you and respond with a single word: Positive, Negative, or Neutral, based on the underlying sentiment of the text."},
                {"role": "user", "content": text}
            ],
            temperature=0.1,
            max_tokens=1  # Ensure only one token (word) is returned
        )
        return response['choices'][0]['message']['content'].strip()  # Strip any extra whitespace
    except openai.error.AuthenticationError as e:
        st.error(f"Authentication Error: {e}")
    except openai.error.OpenAIError as e:
        st.error(f"OpenAI API Error: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

def main():
    st.title("Sentiment Analyzer")
    text = st.text_area("Enter text:")
    if st.button("Analyze"):
        if text.strip():  # Check if text is not empty
            sentiment = get_sentiment(text)
            if sentiment:
                st.write(f"Sentiment: {sentiment}")
                if sentiment == "Positive":
                    st.markdown("<h1 style='text-align: center;'>😊 😄 👍 🌟 💖</h1>", unsafe_allow_html=True)
                elif sentiment == "Negative":
                    st.markdown("<h1 style='text-align: center;'>😡 🙁 👎</h1>", unsafe_allow_html=True)
                else:
                    st.markdown("<h1 style='text-align: center;'>😐</h1>", unsafe_allow_html=True)
        else:
            st.warning("Please enter some text to analyze.")

if __name__ == "__main__":
    main()