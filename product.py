from enum import Enum

from .exceptions import UndefinedProductCategoryError


class ProductCategory(Enum):
    FOOD = 0
    UTENSIL = 1
    ELETRONIC = 2


class Product:
    def __init__(self, id: int, name: str, price: float, weight: float, category: ProductCategory, stock_amount: int, description: str) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.weight = weight
        self.category = category
        self.stock_amount = stock_amount
        self.description = description


    def get_shipment_freight(self):
        """ Returns the percentage of freight applied to the product shipment """

        if self.category == ProductCategory.FOOD:
            return 1.05
        elif self.category == ProductCategory.UTENSIL:
            return 1.12
        elif self.category == ProductCategory.ELETRONIC:
            return 1.35
        else:
            error_message = f'Unknown product category: {self.category}'
            raise UndefinedProductCategoryError(error_message)