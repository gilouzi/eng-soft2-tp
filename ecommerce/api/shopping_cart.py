from __main__ import app
from flask import render_template


@app.route('/shopping_cart')
def shopping_cart_page():
    return render_template('shopping_cart.html')