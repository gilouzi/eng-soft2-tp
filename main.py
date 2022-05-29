from flask import Flask
from flask import render_template
from flask import url_for, redirect
from datetime import timedelta

from ecommerce.models.product import db_product
from ecommerce.models.shopping_cart import ShoppingCart
from ecommerce.models.user import db_user

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
    

# import declared routes
import ecommerce.api.product
import ecommerce.api.shopping_cart
import ecommerce.api.user


if __name__ == '__main__':
    app.run(debug=True)