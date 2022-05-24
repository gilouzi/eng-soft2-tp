class ProductAlreadyAddedError(Exception):
    """ Exception raised when a product has already been added to shopping cart """
    pass


class ProductNotFoundError(Exception):
    """ Exception raised when a product was not found in a shopping cart """
    pass


class UndefinedProductCategoryError(Exception):
    """ Exception raised when a product has an undefined category """
    pass
