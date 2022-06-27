from ecommerce import app
import unittest

from ecommerce.models.user import User
from ecommerce.api.product import save_product
from ecommerce.models.shopping_cart import ShoppingCart
from ecommerce.models.product import db_product, Product, ProductCategory
from ecommerce.api.exceptions import ProductAlreadyAddedError, ProductNotFoundError

class TestShoppingCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super(TestShoppingCart, cls).setUpClass()

        with app.app_context():
            db_product.init_app(app)

            cls.product = Product(
                name='productName',
                price=10.99, 
                weight=0.5,
                category=ProductCategory.UTENSIL,
                stock_amount=5,
                description='productDescription'
            )

            save_product(
                name=cls.product.name,
                price=cls.product.price,
                weight=cls.product.weight,
                category=cls.product.category,
                stock_amount=cls.product.stock_amount,
                description=cls.product.description
            )

    @classmethod
    def tearDownClass(cls) -> None:
        super(TestShoppingCart, cls).tearDownClass()

        with app.app_context():
            product = Product.query.filter(Product.name == 'productName').first()
            db_product.session.delete(product)
            db_product.session.commit()

    def setUp(self):
        with app.app_context():
            user = User(name='userName', email='email@email.com', login='login', password='password', address='address', telephone='123456789')
            
            self.product = TestShoppingCart.product
            self.productId = Product.query.filter(Product.name == 'productName').first().id
            self.shopping_cart = ShoppingCart(user=user)

    def test_add_product(self):
        with app.app_context():
            self.shopping_cart.add_product(self.productId)
            self.assertTrue(self.productId in self.shopping_cart.product_list)
    
    def test_already_added_product(self):
        with app.app_context():
            self.shopping_cart.add_product(self.productId)
            with self.assertRaises(ProductAlreadyAddedError):
                self.shopping_cart.add_product(self.productId)
    
    def test_remove_product(self):
        with app.app_context():
            self.shopping_cart.add_product(self.productId)
            self.shopping_cart.remove_product(self.productId)
            self.assertTrue(self.productId not in self.shopping_cart.product_list)
    
    def test_remove_not_added_product(self):
        with app.app_context():
            with self.assertRaises(ProductNotFoundError):
                self.shopping_cart.remove_product(self.productId)
    
    def test_sub_total(self):
        with app.app_context():
            self.shopping_cart.add_product(self.productId)
            self.assertEqual(self.product.getPrice(), self.shopping_cart.get_sub_total())
    
    def test_total_weight(self):
        with app.app_context():
            self.shopping_cart.add_product(self.productId)
            self.assertEqual(self.product.getWeight(), self.shopping_cart.get_total_weight())
    
    def test_shipping_price(self):
        with app.app_context():
            self.shopping_cart.add_product(self.productId)
            self.assertEqual(self.product.get_shipping_price(), self.shopping_cart.get_shipping())
    
    def test_total_price(self):
        with app.app_context():
            self.shopping_cart.add_product(self.productId)
            self.assertEqual(self.product.getPrice() + self.product.get_shipping_price(), self.shopping_cart.get_total_price())
        