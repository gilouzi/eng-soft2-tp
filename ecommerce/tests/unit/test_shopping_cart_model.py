import unittest
from ecommerce.models.shopping_cart import ShoppingCart

from ecommerce.api.exceptions import ProductNotFoundError
from ecommerce.api.exceptions import ProductAlreadyAddedError


class TestShoppingCartModel(unittest.TestCase):
    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart(None)

    def test_empty_cart_initialization(self) -> None:
        self.assertEqual(self.shopping_cart.length(), 0)

    def test_cart_length_with_one_product(self) -> None:
        self.shopping_cart.add_product(1)
        self.assertEqual(self.shopping_cart.length(), 1)

    def test_cart_length_with_multiple_products(self) -> None:
        self.shopping_cart.add_product(1)
        self.shopping_cart.add_product(2)
        self.shopping_cart.add_product(3)
        self.assertEqual(self.shopping_cart.length(), 3)

    def test_raise_product_already_added_error(self) -> None:
        self.shopping_cart.add_product(1)
        self.shopping_cart.add_product(2)
        self.assertRaises(ProductAlreadyAddedError, self.shopping_cart.add_product, 1)

    def test_raise_product_not_found_error_for_empty_cart(self) -> None:
        self.assertRaises(ProductNotFoundError, self.shopping_cart.remove_product, 0)

    def test_raise_product_not_found_error_for_non_empty_cart(self) -> None:
        self.shopping_cart.add_product(0)
        self.shopping_cart.add_product(1)
        self.shopping_cart.add_product(2)
        self.assertRaises(ProductNotFoundError, self.shopping_cart.remove_product, 3)
