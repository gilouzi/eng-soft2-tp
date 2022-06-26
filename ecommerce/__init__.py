from flask import Flask
from datetime import timedelta
from flask import render_template

from ecommerce.models.user import db_user
from ecommerce.models.product import db_product
from ecommerce.models.order import db_order, db_productsPerOrder
from ecommerce.models.shopping_cart import ShoppingCart


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
    db_order.create_all()
    db_productsPerOrder.create_all()


@app.route('/')
def home():
    return render_template('index_page.html')