from math import prod
from typing import Dict, List

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from ecommerce.models.user import User
from ecommerce.models.product import Product, db_product
from ecommerce.models.payment import PaymentType
from ecommerce.models.shopping_cart import ShoppingCart
from ecommerce.api.exceptions import ProductAlreadyAddedError, ProductNotFoundError

MAX_SIZE_STR = 50

db_order = SQLAlchemy()
db_productsPerOrder = SQLAlchemy()

class Order(db_order.Model):

    __tablename__ = 'order_tb'
    id = db_order.Column(db_order.Integer, primary_key=True)
    user_id = db_order.Column(db_order.Integer)
    total_amount = db_order.Column(db_order.Integer)
    address = db_order.Column(db_order.String(MAX_SIZE_STR))
    payment = db_order.Column(db_order.Enum(PaymentType))

    def __init__(self, userId: int, shoppingCart: ShoppingCart, totalAmount: int, address: str, payment: PaymentType) -> None:
        self.user_id = userId
        self.address = address
        self.payment = payment
        self.shoppingCart = shoppingCart
        self.total_amount = totalAmount

    def save_order(self):
        db_order.session.add(self)
        db_order.session.commit()
        db_order.session.refresh(self)

        order_id = self.id
        for product_id in self.shoppingCart.product_list:
            product = Product.query.filter(Product.id == product_id).first()
            if product:
                productPerOrder = ProductsPerOrder(order_id, product_id)
                db_productsPerOrder.session.add(productPerOrder)
                db_productsPerOrder.session.commit()
                product.stock_amount -= 1
                db_product.session.commit()


    # def add(self, product: Product, quantity=1) -> None:
    #     if product in self.product_list:
    #         self.product_list[product.id] = self.product_list[product.id] + quantity
    #     else:
    #         self.product_list[product.id] = quantity

    # def remove(self, product: Product, quantity=None) -> None:
    #     if product not in self.product_list:
    #         error_message = f'Product with id={product.id} not found'
    #         raise ProductNotFoundError(error_message)

    #     if quantity:
    #         if quantity < self.product_list[product.id]:
    #             self.product_list[product.id] = self.product_list[product.id] - quantity
    #         else:
    #             self.product_list.pop(product.id)
    #     else:
    #         self.product_list.pop(product.id)

    # def finish(self):
    #     pass

class ProductsPerOrder(db_productsPerOrder.Model):

    __tablename__ = 'productsPerOrder_tb'
    id = db_productsPerOrder.Column(db_productsPerOrder.Integer, primary_key=True)
    order_id = db_productsPerOrder.Column(db_productsPerOrder.Integer)
    product_id = db_productsPerOrder.Column(db_productsPerOrder.Integer)

    def __init__(self, orderId: int, productId: int):
        self.order_id = orderId
        self.product_id = productId