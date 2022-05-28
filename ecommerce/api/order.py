from math import prod
from typing import Dict, List

from user import User
from product import Product
from payment import PaymentType
from exceptions import ProductAlreadyAddedError, ProductNotFoundError


class Order:
    def __init__(self, user: User, address: str, payment: PaymentType) -> None:
        self.user = user
        self.address = address
        self.payment = payment

        self.total_price: float = 0
        self.product_list: Dict[Product] = dict()

    def add(self, product: Product, quantity=1) -> None:
        if product in self.product_list:
            self.product_list[product.id] = self.product_list[product.id] + quantity
        else:
            self.product_list[product.id] = quantity

    def remove(self, product: Product, quantity=None) -> None:
        if product not in self.product_list:
            error_message = f'Product with id={product.id} not found'
            raise ProductNotFoundError(error_message)

        if quantity:
            if quantity < self.product_list[product.id]:
                self.product_list[product.id] = self.product_list[product.id] - quantity
            else:
                self.product_list.pop(product.id)
        else:
            self.product_list.pop(product.id)

    def finish(self):
        pass
