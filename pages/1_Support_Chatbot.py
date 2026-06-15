import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬"
)

st.title("💬 MiniStore Support Assistant")

# --------------------------------------------------
# OPENAI CLIENT
# --------------------------------------------------
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# --------------------------------------------------
# PRODUCT CATALOG
# --------------------------------------------------
PRODUCT_CATALOG = """
MiniStore Product Catalog

1. Wireless Headphones
   Price: ₹2999
   Category: Electronics
   Description: Noise-cancelling Bluetooth headphones with long battery life.

2. Smart Watch
   Price: ₹4999
   Category: Electronics
   Description: Fitness tracking smartwatch with notifications and health monitoring.

3. Running Shoes
   Price: ₹2499
   Category: Fashion
   Description: Lightweight and comfortable running shoes.

4. Backpack
   Price: ₹1499
   Category: Accessories
   Description: Durable backpack with laptop compartment.

5. Coffee Maker
   Price: ₹3999
   Category: Home Appliances
   Description: Automatic coffee maker for home use.

6. Gaming Mouse
   Price: ₹1299
   Category: Electronics
   Description: RGB gaming mouse with adjustable DPI.
"""

# --------------------------------------------------
# SYSTEM PROMPT
# --------------------------------------------------
SYSTEM_PROMPT = f"""
You are MiniStore's professional customer support representative.

Your responsibilities:
- Help customers with products.
- Help customers with orders.
- Help customers with delivery questions.
- Help customers with refunds.
- Help customers with returns.
- Help customers with payment methods.
- Help customers understand product details and pricing.

Store Product Catalog:
{PRODUCT_CATALOG}

Rules:
1. Only answer questions related to MiniStore.
2. Allowed topics:
   - Products
   - Orders
   - Delivery
   - Shipping
   - Refunds
   - Returns
   - Payments
   - Product recommendations from the catalog
3. If a user asks unrelated questions such as:
   - General knowledge
   - Programming
   - Politics
   - Science
   - Math
   - Entertainment
   politely explain that you are a MiniStore support assistant and can only help with store-related questions.
4. Be professional, friendly, and concise.
5. Never invent products not listed in the catalog.
"""

# --------------------------------------------------
# CHAT HISTORY
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# USER INPUT
# --------------------------------------------------
user_input = st.chat_input(
    "Ask about products, orders, delivery, refunds, returns, or payments..."
)

if user_input:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Build conversation
    conversation = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    conversation.extend(st.session_state.messages)

    try:

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=conversation,
            temperature=0.3
        )

        assistant_reply = response.choices[0].message.content

    except Exception as e:
        assistant_reply = (
            f"⚠️ Error communicating with OpenAI API:\n\n{str(e)}"
        )

    # Save assistant reply
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)