from typing import List

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
        else:
            self.product_list.append(product_id)
            print("adicionou")

    def remove_product(self, product_id: int) -> None:
        if product_id not in self.product_list:
            error_message = f'Product with id {product_id} not found in shopping cart'
            raise ProductNotFoundError(error_message)

        self.product_list.remove(product_id)

    
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
