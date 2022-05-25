from typing import List

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
        self.product_list: List[Product] = list()

    def add(self, product: Product) -> None:
        if product in self.product_list:
            error_message = f'Product with id={product.id} already added'
            raise ProductAlreadyAddedError(error_message)

        self.product_list.append(product)

    def remove(self, product: Product) -> None:
        if product not in self.product_list:
            error_message = f'Product with id={product.id} not found'
            raise ProductNotFoundError(error_message)

        self.product_list.remove(product)

    def finish(self):
        pass
