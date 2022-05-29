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
        if 'user' in session: 
            user = User.query.filter_by(login=session['user']).first()
            products = []
            sub_total = 0
            shipping = 0
            for product_id in user_cart.product_list:
                product = Product.query.filter(Product.id == product_id).first()
                products.append(product)
                sub_total += product.getPrice()
                shipping = max(product.get_shipping_price(), shipping)
            return render_template('shopping_cart/checkout_page.html', user=user, products=products, sub_total=sub_total, shipping=shipping)
        else:
            flash('You need to be logged in to finish shopping.')
            return redirect('/login')

    if request.method == 'POST':
        name = request.form['name']
        login = request.form['login']
        email = request.form['email']
        address = request.form['address']
        paymentMethod = request.form['paymentMethod']

        products = []
        sub_total = 0
        shipping = 0
        for product_id in user_cart.product_list:
            product = Product.query.filter(Product.id == product_id).first()
            products.append(product)
            sub_total += product.getPrice()
            shipping = max(product.get_shipping_price(), shipping)
        
        # cria pedido
        total_amount = sub_total + shipping
        user = User.query.filter_by(name=name, login=login, email=email).first()
        order = Order(user.id, user_cart, total_amount, address, paymentMethod)
        order.save_order()

        user_cart.product_list = []

        # return redirect('/orders')
        return redirect('/user')