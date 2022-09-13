"""Class file for a franchise

This represents an individual restaurant in the chain and 
can receive orders
"""
from data_models.console_display import ConsoleDisplay
from data_models.order_factory import OrderFactory
from data_models.logger import transaction_log

class Franchise:
    """Represents a single location in the restaurant chain

    Instance Variables:
        location_number: int
            the number that uniquely identifies this location

    Public Methods:
        place_order() -> void
            Allows a single order to be placed based on user choice
            Logs the transaction to a daily log file
    """
    def __init__(self, location_number):
        """Initializes a franchise

        Instance Variables from Parameters:
            location_number: int
                the number that uniquely identifies this location
        """
        self.location_number = location_number

    def place_order(self):
        """Allows a user to place an order and logs the transaction to file

        Effects:
            Displays a welcome message and list of available order types to console
            Logs the user's order to the shared log file
        """
        ConsoleDisplay.display_franchise_welcome(self.location_number)
        order_type = ConsoleDisplay.get_valid_user_input(['pizza', 'salmon', 'spaghetti'], 'To place an order, please enter the number of your menu selection: ')
        new_order = OrderFactory.create_order(order_type)
        transaction_log.log_transaction(new_order, self.location_number)