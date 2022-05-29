from __main__ import app, user_cart
from flask import render_template, request, redirect, session, flash

from ecommerce.models.product import Product
from ecommerce.models.user import User

@app.route('/shopping_cart', methods=['GET', 'POST'])
def shopping_cart_page():
    products = []
    total_amount = 0
    shipping = 0
    for product_id in user_cart.product_list:
        product = Product.query.filter(Product.id == product_id).first()
        products.append(product)
        total_amount += product.getPrice()
        shipping = max(product.get_shipping_price(), shipping)

    if request.method == 'POST':
        if request.form.get('remove_button') == 'remove':
            product_id = int(request.form['product_id'])
            user_cart.remove_product(product_id)
        elif request.form.get('finish_button') == 'finish':
            if not 'user' in session:    
                flash('You need to be logged in to finish shopping.')
            else:
                user = User.query.filter_by(login=session['user']).first()
                return render_template('shopping_cart/checkout_page.html', user=user, products=products, total_amount=total_amount, shipping=shipping)

    products = []
    for product_id in user_cart.product_list:
        product = Product.query.filter(Product.id == product_id).first()
        products.append(product)
        
    return render_template('shopping_cart/shopping_cart_page.html', products=products)

# @app.route('/checkout_page', methods=['GET', 'POST'])
# def checkout_page():
#     if request.method == 'GET':
#         if 'user' in session: 
#             user = User.query.filter_by(login=session['user']).first()
#             products = []
#             total_amount = 0
#             for product_id in user_cart.product_list:
#                 product = Product.query.filter(Product.id == product_id).first()
#                 products.append(product)
#                 total_amount += product.getPrice()
#             return render_template('shopping_cart/checkout_page.html', user=user, products=products, total_amount=total_amount)
#         else:
#             flash('You need to be logged in to finish shopping.')
#             return redirect('/login')

#     if request.method == 'POST':
#         name = request.form['name']
#         login = request.form['login']
#         email = request.form['email']
#         address = request.form['address']

#         print('OK')
#         return redirect('/checkout_page')
