from app import app
import unittest

from ecommerce.models.user import User
from ecommerce.api.product import save_product
from ecommerce.models.shopping_cart import ShoppingCart
from ecommerce.models.product import db_product, Product, ProductCategory
from ecommerce.api.exceptions import ProductAlreadyAddedError, ProductNotFoundError

class testShoppingCart(unittest.TestCase):

    def setUp(self):
        with app.app_context():
            db_product.init_app(app)
            user = User(name='userName', email='email@email.com', login='login', password='password', address='address', telephone='123456789') 
            save_product(name='productName', price=10.99, weight=0.5, category=ProductCategory.UTENSIL, stock_amount=5, description='productDescription')
            productId = Product.query.filter(Product.name == 'productName').first().id
            self.productId = productId
            self.shoppingCart = ShoppingCart(user=user)

    def test_add_product(self):
        with app.app_context():
            self.shoppingCart.add_product(self.productId)
            self.assertTrue(self.productId in self.shoppingCart.product_list)
    
    def test_already_added_product(self):
        with app.app_context():
            self.shoppingCart.add_product(self.productId)
            with self.assertRaises(ProductAlreadyAddedError):
                self.shoppingCart.add_product(self.productId)
    
    def test_remove_product(self):
        with app.app_context():
            self.shoppingCart.add_product(self.productId)
            self.shoppingCart.remove_product(self.productId)
            self.assertTrue(self.productId not in self.shoppingCart.product_list)
    
    def test_remove_not_added_product(self):
        with app.app_context():
            with self.assertRaises(ProductNotFoundError):
                self.shoppingCart.remove_product(self.productId)
            
    


