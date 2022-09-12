from data_models.console_display import ConsoleDisplay
from data_models.order_factory import OrderFactory
from data_models.logger import transaction_log

class Franchise:
    def __init__(self, location_number):
        self.location_number = location_number

    def place_order(self):
        ConsoleDisplay.display_franchise_welcome(self.location_number)
        order_type = ConsoleDisplay.get_valid_user_order_type(['pizza', 'salmon', 'spaghetti'])
        new_order = OrderFactory.create_order(order_type)
        transaction_log.log_transaction(new_order, self.location_number)