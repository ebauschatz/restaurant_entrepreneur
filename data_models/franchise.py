from data_models.console_display import ConsoleDisplay
from data_models.order_factory import OrderFactory

class Franchise:
    def __init__(self, location_number):
        self.location_number = location_number

    def place_order(self):
        ConsoleDisplay.display_franchise_welcome(self.location_number)
        order_type = ConsoleDisplay.get_valid_user_order_type(['pizza', 'salmon', 'spaghetti'])
        new_order = OrderFactory.create_order(order_type)
        # TODO: implement logging
        print(new_order.dish_name)