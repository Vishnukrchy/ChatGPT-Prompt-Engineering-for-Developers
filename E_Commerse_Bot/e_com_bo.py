from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Load product data from a JSON file
def load_products():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Product data file not found. Please ensure 'products.json' exists.")
        return []
    except json.JSONDecodeError:
        print("Error decoding the product data file. Please ensure it is valid JSON.")
        return []


# Function to format product data for the AI
def format_products(products):
    formatted_products = []
    for product in products:
        formatted_product = (
            f"Name: {product['name']}\n"
            f"Category: {product['category']}\n"
            f"Price: ${product['price']}\n"
            f"Description: {product['description']}\n"
            f"Availability: {'In Stock' if product['in_stock'] else 'Out of Stock'}\n"
        )
        formatted_products.append(formatted_product)
    return "\n\n".join(formatted_products)


# Function to handle customer queries
def handle_customer_query(products, user_question):
    # Dynamically adjust the role based on the user's input
    if "shipping" in user_question.lower():
        role = (
            "You are a shipping expert for ShopSmart. "
            "Your task is to answer questions related to shipping times, costs, and policies."
        )
    elif "return" in user_question.lower():
        role = (
            "You are a returns specialist for ShopSmart. "
            "Your task is to guide customers through the return process and explain our return policy."
        )
    elif "product" in user_question.lower() or "recommend" in user_question.lower():
        role = (
            "You are a product recommendation expert for ShopSmart. "
            "Your task is to suggest products based on the customer's preferences and needs."
        )
    else:
        role = (
            "You are a friendly virtual assistant for ShopSmart, an online e-commerce store. "
            "Your goal is to assist customers with general inquiries about products, orders, and policies."
        )

    # Context includes product data and general store information
    context = (
        "ShopSmart offers a wide variety of products including electronics, clothing, home goods, and more. "
        "We provide fast shipping, easy returns, and 24/7 customer support. Here are some key details:\n"
        "- Shipping: Free on orders over $50\n"
        "- Return Policy: 30-day return window\n"
        "- Customer Support: Available via chat, email, or phone\n"
        "- Popular Categories: Electronics, Clothing, Home Decor, Beauty Products\n"
        "- Website: www.shopsmart.com\n"
        "- Contact: support@shopsmart.com | +1-800-555-1234\n"
        f"- Available Products:\n{format_products(products)}"
    )

    # Combine role, context, and user's question into a single prompt
    prompt = f"{role}\n\n{context}\n\nUser's Question: {user_question}"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": role},
                {"role": "user", "content": prompt}
            ]
        )
        ai_response = response.choices[0].message.content
        return ai_response
    except Exception as e:
        return f"Oops! Something went wrong: {e}"


# Main function to run the chatbot
def main():
    print("Welcome to ShopSmart! How can I assist you today?")

    # Load product data from the JSON file
    products = load_products()

    while True:
        user_question = input("\nPlease enter your question (type 'exit' to quit): ")

        if user_question.lower() == 'exit':
            print("Thank you for visiting ShopSmart! Have a great day!")
            break

        # Handle the customer query using the chatbot
        response = handle_customer_query(products, user_question)
        print(f"\nAI Response: {response}")


if __name__ == "__main__":
    main()