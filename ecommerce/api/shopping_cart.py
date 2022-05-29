from __main__ import app, user_cart
from flask import render_template, request

from ecommerce.models.product import Product


@app.route('/shopping_cart', methods=['GET', 'POST'])
def shopping_cart_page():
    products = []
    total_amount = 0
    for product_id in user_cart.product_list:
        product = Product.query.filter(Product.id == product_id).first()
        products.append(product)
        total_amount += product.getPrice()

    if request.method == 'POST':
        if request.form.get('remove_button') == 'remove':
            product_id = int(request.form['product_id'])
            user_cart.remove_product(product_id)
        elif request.form.get('finish_button') == 'finish':
            return render_template('shopping_cart/checkout_page.html', products=products, total_amount=total_amount )

        
    return render_template('shopping_cart/shopping_cart_page.html', products=products)