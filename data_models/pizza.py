"""Class file for a pizza order

Inherits from Order
"""
from data_models.order import Order

class Pizza(Order):
    """Represents a single order of pizza

    Instance Variables from Parent:
        dish_name: str
            the name of the dish that can be ordered
        price: int
            the cost of the dish 
    """
    def __init__(self, dish_name, price):
        """Initializes a pizza order

        Instance Variables from Parent:
            dish_name: str
                the name of the dish that can be ordered
            price: int
                the cost of the dish
        """
        super().__init__(dish_name, price)