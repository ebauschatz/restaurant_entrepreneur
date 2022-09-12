from data_models.pizza import Pizza
from data_models.spaghetti import Spaghetti
from data_models.salmon import Salmon


class OrderFactory:
    @staticmethod
    def create_order(order_type):
        if order_type == 'pizza':
            return Pizza('pizza', 15)
        elif order_type == 'salmon':
            return Salmon('salmon', 17)
        elif order_type == 'spaghetti':
            return Spaghetti('spaghetti', 11)