import json
import argparse

from flask import Flask
from flask import render_template
from flask import url_for, redirect
from datetime import timedelta

from ecommerce.models.product import db_product
from ecommerce.models.shopping_cart import ShoppingCart
from ecommerce.models.user import db_user
from ecommerce.models.product import Product, ProductCategory


app = Flask(__name__)
app.secret_key = "eng-soft2-tp"
app.permanent_session_lifetime = timedelta(minutes=20)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_product.init_app(app)
user_cart = ShoppingCart(None)


@app.before_first_request
def create_database():
    db_product.create_all()
    db_user.create_all()


@app.route('/')
def home():
    return render_template('index.html')


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--default-db', dest='create_default_db', action='store_true', required=False, help='flag to create a default database')

    args = parser.parse_args()
    return args


def create_default_database():
    with open('default_products.json', 'r') as f:
        products = json.load(f)

    for product in products:
        product['category'] = ProductCategory[product['category']]
        p = Product(**product)
        


# import declared routes
import ecommerce.api.product
import ecommerce.api.shopping_cart
import ecommerce.api.user


if __name__ == '__main__':
    args = parse_command_line_arguments()
    if args.create_default_db:
        print('[warning] Creating default database...')
        create_default_database()

    app.run(debug=True)