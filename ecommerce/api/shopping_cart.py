from __main__ import app, user_cart
from flask import render_template, request, session, flash

from ecommerce.models.product import Product
from ecommerce.models.user import User

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
                user = User.query.filter_by(login=session['user']).first()
                flash(f'{user.getName()}, we are finalizing your purchase.')
    products = []
    for product_id in user_cart.product_list:
        product = Product.query.filter(Product.id == product_id).first()
        products.append(product)
        
    return render_template('shopping_cart/shopping_cart_page.html', products=products)