# Instructions to Set Up and Run the Application

# 1. Create and activate a virtual environment:
# On macOS/Linux:
#   python3 -m venv venv
#   source venv/bin/activate
# On Windows:
#   python -m venv venv
#   venv\\Scripts\\activate

# 2. Install dependencies:
#   pip install flask

# 3. Save the following code into a file (e.g., app.py):

from flask import Flask, render_template_string, request

app = Flask(__name__)

# Basic CSS styling
base_css = """
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        text-align: center;
        margin: 0;
        padding: 0;
    }
    header {
        background-color: #4CAF50;
        color: white;
        padding: 1em 0;
        font-size: 1.5em;
    }
    .container {
        margin: 2em auto;
        max-width: 600px;
        background: white;
        padding: 2em;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
    }
    button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
    }
    button:hover {
        background-color: #45a049;
    }
    .product-list {
        display: flex;
        flex-direction: column;
        gap: 1em;
        align-items: center;
    }
    .product-item {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 1em;
        width: 80%;
        background: #fafafa;
        box-shadow: 0px 0px 5px rgba(0,0,0,0.05);
    }
</style>
"""

# Product data
products = [
    {"id": 1, "name": "Awesome SaaS Subscription", "desc": "Only $9.99/month. Cancel anytime.", "price": "$9.99/month"},
    {"id": 2, "name": "Pro Analytics Add-on", "desc": "Advanced analytics for your business.", "price": "$4.99/month"},
    {"id": 3, "name": "Priority Support", "desc": "24/7 support for your team.", "price": "$2.99/month"},
]

# Homepage template
home_template = base_css + """
<header>My Simple SaaS Store</header>
<div class="container">
    <h2>Welcome to the Store</h2>
    <p>Click below to view our products.</p>
    <form action="/products">
        <button type="submit">View Products</button>
    </form>
</div>
"""

# Products page template
products_template = base_css + """
<header>Products</header>
<div class="container">
    <h2>Choose a Product</h2>
    <div class="product-list">
        {% for product in products %}
        <div class="product-item">
            <h3>{{ product.name }}</h3>
            <p>{{ product.desc }}</p>
            <strong>{{ product.price }}</strong>
            <form action="/checkout" method="get">
                <input type="hidden" name="product_id" value="{{ product.id }}">
                <button type="submit">Buy Now</button>
            </form>
        </div>
        {% endfor %}
    </div>
    <br>
    <a href="/">Return Home</a>
</div>
"""

# Checkout page template
checkout_template = base_css + """
<header>Checkout</header>
<div class="container">
    <h2>Thank You!</h2>
    <p>Your purchase of <strong>{{ product_name }}</strong> has been confirmed.</p>
    <a href="/">Return Home</a>
</div>
"""

@app.route("/")
def home():
    return render_template_string(home_template)

@app.route("/products")
def products_page():
    return render_template_string(products_template, products=products)

@app.route("/checkout")
def checkout():
    product_id = request.args.get("product_id", type=int)
    product_name = next((p["name"] for p in products if p["id"] == product_id), "Unknown Product")
    return render_template_string(checkout_template, product_name=product_name)

app.run(host="0.0.0.0",port=8080)