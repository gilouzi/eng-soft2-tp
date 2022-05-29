from __main__ import app, user_cart
from flask import render_template, request

from ecommerce.models.product import Product


@app.route('/shopping_cart', methods=['GET', 'POST'])
def shopping_cart_page():
    if request.method == 'POST':
        if request.form.get('remove_button') == 'remove':
            product_id = int(request.form['product_id'])
            user_cart.remove_product(product_id)
        elif request.form.get('finish_button') == 'finish':
            print('Terminei')

    products = []
    for product_id in user_cart.product_list:
        product = Product.query.filter(Product.id == product_id).first()
        products.append(product)
        
    return render_template('shopping_cart.html', products=products)