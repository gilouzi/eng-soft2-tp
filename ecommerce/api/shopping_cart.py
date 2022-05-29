from __main__ import app, user_cart
from flask import render_template, request, redirect, session, flash, url_for

from ecommerce.models.product import Product
from ecommerce.models.user import User
from ecommerce.models.order import Order, ProductsPerOrder

@app.route('/shopping_cart', methods=['GET', 'POST'])
def shopping_cart_page():

    if request.method == 'POST':
        if request.form.get('remove_button') == 'remove':
            product_id = int(request.form['product_id'])
            user_cart.remove_product(product_id)
        elif request.form.get('finish_button') == 'finish':
            if not 'user' in session:    
                flash('You need to be logged in to finish shopping.')
            else:
                return redirect(url_for('checkout_page'))

    products = user_cart.get_products() 
    return render_template('shopping_cart/shopping_cart_page.html', products=products)

@app.route('/orders', methods=['GET', 'POST'])
def read_orders():
    orders = Order.query.all()
    productsPerOrder = ProductsPerOrder.query.all()
    
    return render_template('orders.html', orders=orders, productsPerOrder=productsPerOrder)

@app.route('/checkout_page', methods=['GET', 'POST'])
def checkout_page():
    if request.method == 'GET':
        return show_checkout()

    if request.method == 'POST':
        return create_order(request.form)

def show_checkout():
    if 'user' in session: 
        user = User.query.filter_by(login=session['user']).first()
        sub_total = user_cart.get_sub_total()
        shipping = user_cart.get_shipping() 
        products = user_cart.get_products()
        return render_template('shopping_cart/checkout_page.html', user=user, products=products, sub_total=sub_total, shipping=shipping)
    else:
        flash('You need to be logged in to finish shopping.')
        return redirect('/login')

def create_order(form):
    name = form['name']
    login = form['login']
    email = form['email']
    address = form['address']
    paymentMethod = form['paymentMethod']

    sub_total = user_cart.get_sub_total()
    shipping = user_cart.get_shipping() 
    
    total_amount = sub_total + shipping
    user = User.query.filter_by(name=name, login=login, email=email).first()
    order = Order(user.id, user_cart, total_amount, address, paymentMethod)
    order.save_order()

    user_cart.product_list = []

    return redirect('/user')