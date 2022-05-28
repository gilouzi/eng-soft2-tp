from flask import render_template, request, redirect
from __main__ import app

from ecommerce.models.product import db_product, Product

def save_product(id, name, price, weight, category, stock_amount, description):
    product = Product(id, name, price, weight, category, stock_amount, description)
    db_product.session.add(product)
    db_product.session.commit()

@app.route('/product')
def read_product():
    products = Product.query.all()
    return render_template('product/read.html', products=products)

@app.route('/product/create/', methods=['GET', 'POST'])
def create_product():
    if request.method == 'GET':
        return render_template('product/create.html')
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        price = request.form['price']
        weight = request.form['weight']
        category = request.form['category']
        stock_amount = request.form['stock_amount']
        description = request.form['description']
        save_product(id, name, price, weight, category, stock_amount, description)
        return redirect('/product')
