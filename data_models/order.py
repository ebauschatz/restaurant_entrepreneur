"""Class file for orders

Parent for any type of order that can be placed at a franchise
"""
class Order:
    """Represents any type of order that can be placed at a franchise

    Instance Variables:
        dish_name: str
            the name of the dish that can be ordered
        price: int
            the cost of the dish
    """
    def __init__(self, dish_name, price):
        """Initializes an order

        Instance Variables from Parameters:
            dish_name: str
                the name of the dish that can be ordered
            price: int
                the cost of the dish
        """
        self.dish_name = dish_name
        self.price = price