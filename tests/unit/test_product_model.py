import unittest
from ecommerce.models.product import Product, ProductCategory

class TestProductModel(unittest.TestCase):
    def test_food_shipping_price(self):
        product = Product("food product", 100, 12, ProductCategory.FOOD, 10, "test food")
        self.assertEqual(5, product.get_shipping_price())