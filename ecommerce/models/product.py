from enum import Enum
from math import ceil

from ecommerce.api.exceptions import UndefinedProductCategoryError
from flask_sqlalchemy import SQLAlchemy
MAX_SIZE_STR = 50

db_product = SQLAlchemy()

class ProductCategory(Enum):
    FOOD = 0
    UTENSIL = 1
    ELETRONIC = 2


class Product(db_product.Model):

    __tablename__ = "product_tb"

    id = db_product.Column(db_product.Integer, primary_key=True)
    name = db_product.Column(db_product.String(MAX_SIZE_STR))
    price = db_product.Column(db_product.Float)
    shipping_price = db_product.Column(db_product.Float)
    weight = db_product.Column(db_product.Float)
    category = db_product.Column(db_product.Enum(ProductCategory))
    stock_amount = db_product.Column(db_product.Integer)
    description = db_product.Column(db_product.String(MAX_SIZE_STR))

    def __init__(self, name: str, price: float, weight: float, category: ProductCategory, stock_amount: int, description: str) -> None:
        self.name = name
        self.price = price
        self.weight = weight
        self.category = category
        self.stock_amount = stock_amount
        self.description = description
        self.shipping_price = self.set_shipping_price(category, price)

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getWeight(self):
        return self.weight
    
    def getCategory(self):
        return self.category.name
    
    def getStockAmount(self):
        return self.stock_amount

    def getDescription(self):
        return self.description

    def get_shipping_price(self):
        """ Returns the percentage of freight applied to the product shipment """
        return self.shipping_price

    def get_rounded_price(self, price):
        return ceil(price * 100) / 100
    
    def set_shipping_price(self, category, price):
        if category == ProductCategory.FOOD:
            return self.get_rounded_price(0.05*price)
        elif category == ProductCategory.UTENSIL:
            return self.get_rounded_price(0.12*price)
        elif category == ProductCategory.ELETRONIC:
            return self.get_rounded_price(0.35*price)
        else:
            error_message = f'Unknown product category: {category}'
            raise UndefinedProductCategoryError(error_message)