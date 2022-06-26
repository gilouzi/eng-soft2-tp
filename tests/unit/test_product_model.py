import unittest
from ecommerce.api.exceptions import UndefinedProductCategoryError
from ecommerce.models.product import Product, ProductCategory

class TestProductModel(unittest.TestCase):
    def setUp(self) -> None:
        self.product = Product('test product', 0, 0, None, 0, 'test product')

    def test_food_shipping_price(self):
        self.product.price = 100
        self.product.category = ProductCategory.FOOD
        self.assertEqual(5, self.product.get_shipping_price())

    def test_utensil_shipping_price(self):
        self.product.price = 100
        self.product.category = ProductCategory.UTENSIL
        self.assertEqual(12, self.product.get_shipping_price())
    
    def test_eletronic_shipping_price(self):
        self.product.price = 100
        self.product.category = ProductCategory.ELETRONIC
        self.assertEqual(35, self.product.get_shipping_price())
    
    def test_raise_undefined_product_category_error(self):
        self.product.category = 'UNDEFINED'
        self.assertRaises(UndefinedProductCategoryError, self.product.get_shipping_price)

    def test_food_shipping_price_rouding(self):
        self.product.price = 1.50
        self.product.category = ProductCategory.FOOD
        self.assertEqual(0.08, self.product.get_shipping_price())
    
    def test_utensil_shipping_price_rouding(self):
        self.product.price = 1.55
        self.product.category = ProductCategory.UTENSIL
        self.assertEqual(0.19, self.product.get_shipping_price())

    def test_eletronic_shipping_price_rounding(self):
        self.product.price = 1.50
        self.product.category = ProductCategory.ELETRONIC
        self.assertEqual(0.53, self.product.get_shipping_price())
