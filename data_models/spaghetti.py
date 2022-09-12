"""Class file for a spaghetti order

Inherits from Order
"""
from data_models.order import Order

class Spaghetti(Order):
    """Represents a single order of spaghetti

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