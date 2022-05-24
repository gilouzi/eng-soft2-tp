from typing import List

from .user import User
from .product import Product

from .exceptions import ProductNotFoundError
from .exceptions import ProductAlreadyAddedError


class ShoppingCart:
    def __init__(self, user: User) -> None:
        self.user = user
        self.product_list: List[Product] = list()
    

    def add_product(self, product: Product) -> None:
        if product in self.product_list:
            error_message = f'Product with id {product.id} already added to shopping cart'
            raise ProductAlreadyAddedError(error_message)
        
        self.product_list.append(product)


    def remove_product(self, product: Product) -> None:
        if product not in self.product_list:
            error_message = f'Product with id {product.id} not found in shopping cart'
            raise ProductNotFoundError(error_message)

        self.product_list.remove(product)

    
    def get_total_weight(self) -> float:
        total_weight = 0
        for product in self.product_list:
            total_weight += product.weight

        return total_weight


    def get_total_price(self) -> float:
        total_price = 0
        for product in self.product_list:
            product_price_with_shipment = product.get_shipment_freight() * product.price
            total_price += product_price_with_shipment

        return total_price
