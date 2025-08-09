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


from flask import Flask, render_template_string, url_for, redirect

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
</style>
"""

# Homepage template
home_template = base_css + """
<header>My Simple SaaS Store</header>
<div class="container">
    <h2>Welcome to the Store</h2>
    <p>Click below to view our featured product.</p>
    <form action="/product">
        <button type="submit">View Product</button>
    </form>
</div>
"""

# Product page template
product_template = base_css + """
<header>Product Page</header>
<div class="container">
    <h2>Awesome SaaS Subscription</h2>
    <p>Only $9.99/month. Cancel anytime.</p>
    <form action="/checkout">
        <button type="submit">Buy Now</button>
    </form>
</div>
"""

# Checkout page template
checkout_template = base_css + """
<header>Checkout</header>
<div class="container">
    <h2>Thank You!</h2>
    <p>Your purchase has been confirmed.</p>
    <a href="/">Return Home</a>
</div>
"""

@app.route("/")
def home():
    return render_template_string(home_template)

@app.route("/product")
def product():
    return render_template_string(product_template)

@app.route("/checkout")
def checkout():
    return render_template_string(checkout_template)

app.run(host="0.0.0.0",port=8080)