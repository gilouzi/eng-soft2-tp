from typing import List
from ecommerce.models.product import Product

from ecommerce.models.user import User

from ecommerce.api.exceptions import ProductNotFoundError
from ecommerce.api.exceptions import ProductAlreadyAddedError


class ShoppingCart:
    def __init__(self, user: User) -> None:
        self.user = user
        self.product_list: List[int] = list()

    def add_product(self, product_id: int) -> None:
        if product_id in self.product_list:
            error_message = f'Product with id {product_id} already added to shopping cart'
            raise ProductAlreadyAddedError(error_message)
        
        self.product_list.append(product_id)

    def remove_product(self, product_id: int) -> None:
        if product_id not in self.product_list:
            error_message = f'Product with id {product_id} not found in shopping cart'
            raise ProductNotFoundError(error_message)

        self.product_list.remove(product_id)

    def length(self) -> int:
        return len(self.product_list)

    def get_sub_total(self) -> float:
        subtotal = 0
        for product_id in self.product_list:
            product = self.get_product_by_id(product_id)
            subtotal += product.price

        return subtotal
    
    def get_shipping(self) -> float:
        shipping = 0
        for product_id in self.product_list:
            product = self.get_product_by_id(product_id)
            shipping = max(shipping, product.get_shipping_price())

        return shipping

    def get_total_weight(self) -> float:
        total_weight = 0
        for product in self.product_list:
            total_weight += product.weight

        return total_weight

    def get_total_price(self) -> float:
        total_price = 0
        for product in self.product_list:
            product_price_with_shipment = product.get_shipping_price() * product.price
            total_price += product_price_with_shipment

        return total_price

    def get_products(self) -> List[Product]:
        products = []
        for product_id in self.product_list:
            product = self.get_product_by_id(product_id)
            products.append(product)
        
        return products
    
    def get_product_by_id(self, id):
        return Product.query.filter(Product.id == id).first()
