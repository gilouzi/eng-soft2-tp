import unittest
from ecommerce.api.exceptions import UndefinedProductCategoryError
from ecommerce.models.product import Product, ProductCategory

class TestProductModel(unittest.TestCase):
    def test_book_shipping_price(self):
        product = Product('test product', 100, 0, ProductCategory.BOOK, 0, 'test product')
        self.assertEqual(1, product.get_shipping_price())

    def test_food_shipping_price(self):
        product = Product('test product', 100, 0, ProductCategory.FOOD, 0, 'test product')
        self.assertEqual(5, product.get_shipping_price())

    def test_utensil_shipping_price(self):
        product = Product('test product', 100, 0, ProductCategory.UTENSIL, 0, 'test product')
        self.assertEqual(12, product.get_shipping_price())
    
    def test_eletronic_shipping_price(self):
        product = Product('test product', 100, 0, ProductCategory.ELETRONIC, 0, 'test product')
        self.assertEqual(35, product.get_shipping_price())
    
    def test_raise_undefined_product_category_error(self):
        with self.assertRaises(UndefinedProductCategoryError):
            Product('test product', 100, 0, 'UNDEFINED', 0, 'test product')

    def test_book_shipping_price_rounding(self):
        product = Product('test product', 1.43, 0, ProductCategory.BOOK, 0, 'test product')
        self.assertEqual(0.02, product.get_shipping_price())

    def test_food_shipping_price_rouding(self):
        product = Product('test product', 1.50, 0, ProductCategory.FOOD, 0, 'test product')
        self.assertEqual(0.08, product.get_shipping_price())
    
    def test_utensil_shipping_price_rouding(self):
        product = Product('test product', 1.55, 0, ProductCategory.UTENSIL, 0, 'test product')
        self.assertEqual(0.19, product.get_shipping_price())

    def test_eletronic_shipping_price_rounding(self):
        product = Product('test product', 1.50, 0, ProductCategory.ELETRONIC, 0, 'test product')
        self.assertEqual(0.53, product.get_shipping_price())
