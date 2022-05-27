from flask import Flask
from flask import render_template
from flask import url_for, redirect


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/products')
def products_page():
    products = [f'produto-{i}' for i in range(1, 11)]
    return render_template('products.html', products=products)


@app.route('/shopping_cart')
def shopping_cart_page():
    return render_template('shopping_cart.html')


if __name__ == '__main__':
    app.run(debug=True)
