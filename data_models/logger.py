"""Class file for logging functionality

Handles overall transaction tracking and logging
A Logger is intantiated at the bottom of this file, and
this instance should be imported and used instead of the class
"""
import datetime

class Logger:
    """Represents all logging and tracking functionality
    
    Instance Variables:
        transaction_count: int
            a running count of the total transactions during this run of the application
        daily_sales: int
            a running total of the cost of all orders placed across franchises

    Public Methods:
        log_transaction(Order, int) -> void
            adds a transaction entry to the log
            increments the transaction_count and daily_sales instance variables
        initialize_daily_log() -> void
            Clears any existing log information and adds today's date to the top of the file
    """
    def __init__(self):
        """Initializes a logger

        Instance Variables:
            transaction_count: int
                a running count of the total transactions during this run of the application
            daily_sales: int
                a running total of the cost of all orders placed across franchises
        """
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self, order, franchise_number):
        """Log a single transaction to file and adjust running totals

        Args:
            order: Order
                a single order to log
            franchise_number: int
                the number of the franchise where the order was placed

        Effects:
            Logs order information to a file
            Updates the transaction_count and daily_sales instance variables
        """
        self.transaction_count += 1
        self.daily_sales += order.price

        current_local_time = datetime.datetime.now().strftime('%X')
        log_file = open('log.txt', 'a')
        log_file.write(f'''\n[{current_local_time}] - Transaction #{self.transaction_count}
        Order Type: {order.dish_name.title()}
        Order Price: ${order.price}
        Franchise Number: {franchise_number}
        Running Daily Sales Total: ${self.daily_sales}''')
        log_file.close()

    def initialize_daily_log(self):
        """Clears log file and sets file header message

        Effects:
            Clears any text currently in the file
            Sets file header row and today's date
        """
        log_file = open('log.txt', 'w')
        log_file.write(f'Transaction Log for {datetime.datetime.now().strftime("%x")}')

transaction_log = Logger()