from flask import Flask
from flask import render_template
from flask import url_for, redirect

from ecommerce.models.product import db_product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_product.init_app(app)

@app.before_first_request
def create_database():
    db_product.create_all()

@app.route('/')
def home():
    return render_template('index.html')
    

# import declared routes
import ecommerce.api.product
import ecommerce.api.shopping_cart


if __name__ == '__main__':
    app.run(debug=True)