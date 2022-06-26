import unittest
from ecommerce.api.exceptions import UndefinedProductCategoryError
from ecommerce.models.product import Product, ProductCategory

class TestProductModel(unittest.TestCase):

    def test_food_shipping_price(self):
        product = Product("food product", 100, 12, ProductCategory.FOOD, 10, "test food")
        self.assertEqual(5, product.get_shipping_price())

    def test_utensil_shipping_price(self):
        product = Product("utensil product", 100, 12, ProductCategory.UTENSIL, 10, "test utensil")
        self.assertEqual(12, product.get_shipping_price())
    
    def test_eletronic_shipping_price(self):
        product = Product("eletronic product", 100, 12, ProductCategory.ELETRONIC, 10, "test eletronic")
        self.assertEqual(35, product.get_shipping_price())
    
    def test_raise_undefined_product_category_error(self):
        product = Product("undefined product", 100, 12, "UNDEFINED", 10, "test undefined")
        self.assertRaises(UndefinedProductCategoryError, product.get_shipping_price)

    def test_food_shipping_price_rouding(self):
        product = Product("food product", 1.50, 12, ProductCategory.FOOD, 10, "test food")
        self.assertEqual(0.08, product.get_shipping_price())
    
    def test_utensil_shipping_price_rouding(self):
        product = Product("utensil product", 1.55, 12, ProductCategory.UTENSIL, 10, "test utensil")
        self.assertEqual(0.19, product.get_shipping_price())

    def test_eletronic_shipping_price(self):
        product = Product("eletronic product", 1.50, 12, ProductCategory.ELETRONIC, 10, "test eletronic")
        self.assertEqual(0.53, product.get_shipping_price())