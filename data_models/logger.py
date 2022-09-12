import datetime

class Logger:
    def __init__(self):
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self, order, franchise_number):
        self.transaction_count += 1
        self.daily_sales += order.price

        current_local_time = datetime.datetime.now().strftime('%X')
        log_file = open('log.txt', 'a')
        log_file.write(f'''\n[{current_local_time}] - Transaction #{self.transaction_count}
        Order Type: {order.dish_name.title()}
        Order Price: {order.price}
        Franchise Number: {franchise_number}
        Running Daily Sales Total: {self.daily_sales}''')
        log_file.close()

    def initialize_daily_log(self):
        log_file = open('log.txt', 'w')
        log_file.write(f'Transaction Log for {datetime.datetime.now().strftime("%x")}')

transaction_log = Logger()