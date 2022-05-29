import json

from flask import render_template, request, redirect
from __main__ import app, user_cart

from ecommerce.models.product import db_product, Product, ProductCategory


def save_product(name, price, weight, category, stock_amount, description):
    product = Product(name, price, weight, category, stock_amount, description)
    db_product.session.add(product)
    db_product.session.commit()


def insert_default_products_in_database():
    products_json = 'default_products.json'
    with open(products_json, 'r') as file:
        products = json.load(file)

    for product in products:
        product['category'] = ProductCategory[product['category']]
        save_product(**product)


@app.route('/product', methods=['GET', 'POST'])
def read_product():
    if request.method == 'POST':
        product_id = int(request.form['product_id'])
        if request.form['cart_button'] == 'add_product':
            user_cart.add_product(product_id)
        elif request.form['cart_button'] == 'remove_product':
            user_cart.remove_product(product_id)

    products = Product.query.all()
    product_list = user_cart.product_list
    
    return render_template('product/list_product_page.html', products=products, product_list=product_list)

@app.route('/product/create/', methods=['GET', 'POST'])
def create_product():
    if request.method == 'GET':
        return render_template('product/create_product_page.html')

    if request.method == 'POST':
        if request.form.get('button') == 'insert-default-products':
            insert_default_products_in_database()
        else:
            name = request.form['name']
            price = request.form['price']
            weight = request.form['weight']
            category = request.form['category']
            stock_amount = request.form['stock_amount']
            description = request.form['description']
            save_product(name, price, weight, category, stock_amount, description)
        
        return redirect('/product')
