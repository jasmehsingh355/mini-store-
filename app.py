import streamlit as st

st.set_page_config(
    page_title="MiniStore",
    page_icon="🛒",
    layout="wide"
)

# -----------------------
# CUSTOM CSS
# -----------------------
st.markdown("""
<style>

.title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#2c3e50;
}

.product-card{
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0 2px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

/* Floating Support Button */
.support-btn {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background-color: #2563eb;
    color: white;
    padding: 15px 20px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    z-index: 9999;
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# PRODUCTS
# -----------------------
products = [
    {
        "name":"Wireless Headphones",
        "price":2999,
        "description":"Noise cancelling Bluetooth headphones",
        "category":"Electronics"
    },
    {
        "name":"Smart Watch",
        "price":4999,
        "description":"Fitness tracking smartwatch",
        "category":"Electronics"
    },
    {
        "name":"Running Shoes",
        "price":2499,
        "description":"Comfortable running shoes",
        "category":"Fashion"
    },
    {
        "name":"Backpack",
        "price":1499,
        "description":"Laptop backpack",
        "category":"Accessories"
    },
    {
        "name":"Coffee Maker",
        "price":3999,
        "description":"Automatic coffee machine",
        "category":"Home Appliances"
    },
    {
        "name":"Gaming Mouse",
        "price":1299,
        "description":"RGB gaming mouse",
        "category":"Electronics"
    }
]

# -----------------------
# CART
# -----------------------
if "cart_count" not in st.session_state:
    st.session_state.cart_count = 0

# -----------------------
# SIDEBAR
# -----------------------
st.sidebar.title("🛍 Categories")

categories = ["All"] + list(
    set([p["category"] for p in products])
)

selected = st.sidebar.radio(
    "Select Category",
    categories
)

st.sidebar.markdown("---")

st.sidebar.subheader("🛒 Cart")
st.sidebar.write(
    f"Items: {st.session_state.cart_count}"
)

# -----------------------
# HOMEPAGE
# -----------------------
st.markdown(
    '<div class="title">🛒 MiniStore</div>',
    unsafe_allow_html=True
)

st.markdown("""
### Welcome to MiniStore

Discover premium products at affordable prices.
""")

st.header("⭐ Featured Products")

filtered_products = products

if selected != "All":
    filtered_products = [
        p for p in products
        if p["category"] == selected
    ]

cols = st.columns(3)

for i, product in enumerate(filtered_products):

    with cols[i % 3]:

        st.markdown(f"""
        <div class="product-card">
            <h3>{product['name']}</h3>
            <p>{product['description']}</p>
            <h4>₹{product['price']}</h4>
            <p>{product['category']}</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "Add To Cart",
            key=product["name"]
        ):
            st.session_state.cart_count += 1

# -----------------------
# FLOATING SUPPORT BUTTON
# -----------------------
st.markdown("""
<a class="support-btn"
href="/Support_Chatbot"
target="_self">
💬 Support
</a>
""",
unsafe_allow_html=True)