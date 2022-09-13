"""Class file for logging functionality

Handles overall transaction tracking and logging
A Logger is intantiated at the bottom of this file, and
this instance should be imported and used instead of the class
"""
import datetime
import os
from data_models.console_display import ConsoleDisplay

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
        determine_log_mode() - > void
            Determines if the log should be initialized or if new entries should append to the
            end of the existing log. If appending, also resets the transaction_count and daily_sales
            instance variables to the last recorded values
        initialize_daily_log() -> void
            Clears any existing log information and adds today's date to the top of the file
        resume_daily_log() -> void
            Resumes logging and retains existing log data
        set_log_counters_from_log() -> void
            Sets log instance variables to last logged values
        record_application_finished() -> void
            Adds a log entry showing the date and time the application finished
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

    def determine_log_mode(self):
        """Determine if new log entries should append to the previous log, or restart from a blank file

        Effects:
            Based on user decision, will either remove existing contents of the log file and start over,
            or append to the existing data with a resuming message and continue counters from the last
            logged value
        """
        if os.path.getsize('log.txt') == 0:
            self.initialize_daily_log()
        else:
            ConsoleDisplay.display_existing_log_data_found()
            log_mode = ConsoleDisplay.get_valid_user_input(['resume', 'restart'], 'Please enter the number of the log option you desire: ')
            if log_mode == 'resume':
                self.resume_daily_log()
            else:
                self.initialize_daily_log()
    
    def initialize_daily_log(self):
        """Clears log file and sets file header message

        Effects:
            Clears any text currently in the file
            Sets file header row and today's date
        """
        current_local_datetime = datetime.datetime.now()
        log_file = open('log.txt', 'w')
        log_file.write(f'Transaction Log for {current_local_datetime.strftime("%m/%d/%Y")}\n')
        log_file.write(f'\nApplication starting at {current_local_datetime.strftime("%H:%M:%S")}\n')
        log_file.close()

    def resume_daily_log(self):
        """Resumes existing logging

        Effects:
            Adds log message when application resumes
            Resets instance variables to last logged values
        """
        self.set_log_counters_from_log()

        current_local_datetime = datetime.datetime.now()
        log_file = open('log.txt', 'a')
        log_file.write(f'\n\nApplication resuming at {current_local_datetime.strftime("%m/%d/%Y %H:%M:%S")}\n')
        log_file.close()

    def set_log_counters_from_log(self):
        """Resets log counters to last logged values
        Note if log file size grows unexpectedly it may be necessary to change the
        method of retrieving these values from enumerate() to something more performant

        Effects:
            Resets transaction_count and daily_sales instance variables to last logged values
        """
        log = open('log.txt', 'r')
        for _, line in enumerate(log):
            if 'Transaction #' in line:
                transaction = line.split('#')[1]
                self.transaction_count = int(transaction)
            elif 'Daily Sales Total' in line:
                sales_total = line.split('$')[1]
                self.daily_sales = int(sales_total)
        
    def log_transaction(self, order, franchise_number):
        """Log a single transaction to file and adjust running totals

        Note if changing log format: Ensure the method used to reset instance
        variables to last logged value still works or make any necessary
        changes to self.set_log_counters_from_log()

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

    def record_application_finished(self):
        """Adds a log entry showing the date and time the application finished

        Effects:
            Adds a log entry when the application finishes
        """
        current_local_datetime = datetime.datetime.now()
        log_file = open('log.txt', 'a')
        log_file.write(f'\n\nApplication finished at {current_local_datetime.strftime("%m/%d/%Y %H:%M:%S")}')
        log_file.close()

transaction_log = Logger()