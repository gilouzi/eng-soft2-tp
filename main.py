from ecommerce import app


# import declared routes
import ecommerce.api.product
import ecommerce.api.shopping_cart
import ecommerce.api.user

if __name__ == '__main__':
    app.run(debug=True)