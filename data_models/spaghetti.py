from data_models.order import Order

class Spaghetti(Order):
    def __init__(self, dish_name, price):
        super().__init__(dish_name, price)