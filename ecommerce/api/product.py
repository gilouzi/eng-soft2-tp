from flask import render_template, request, redirect
from __main__ import app, user_cart

from ecommerce.models.product import db_product, Product


def save_product(name, price, weight, category, stock_amount, description):
    product = Product(name, price, weight, category, stock_amount, description)
    db_product.session.add(product)
    db_product.session.commit()


@app.route('/product', methods=['GET', 'POST'])
def read_product():
    if request.method == 'POST':
        print('adicionei')
        user_cart.add_product(int(request.form['cart_button']))

    products = Product.query.all()
    return render_template('product/read.html', products=products, product_list=user_cart.product_list)

@app.route('/product/create/', methods=['GET', 'POST'])
def create_product():
    if request.method == 'GET':
        return render_template('product/create.html')
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        weight = request.form['weight']
        category = request.form['category']
        stock_amount = request.form['stock_amount']
        description = request.form['description']
        save_product(name, price, weight, category, stock_amount, description)
        return redirect('/product')
