"""Class file for the order factory

Used to create an order of a given type
All orders returned should inherit from the Order class
"""
from data_models.pizza import Pizza
from data_models.spaghetti import Spaghetti
from data_models.salmon import Salmon


class OrderFactory:
    """Factory for generating an individual order

    Public Static Methods:
        create_order(str) -> Order
            given a string order type, returns an order of the appropriate subtype
    """
    @staticmethod
    def create_order(order_type):
        """Creates an order of a specified type

        Args:
            order_type: str
                the type of order to be created
        
        Returns:
            An object with a type that is a child class of Order
        """
        if order_type == 'pizza':
            return Pizza('pizza', 15)
        elif order_type == 'salmon':
            return Salmon('salmon', 17)
        elif order_type == 'spaghetti':
            return Spaghetti('spaghetti', 11)