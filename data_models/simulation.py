from data_models.franchise import Franchise
from data_models.logger import transaction_log

class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        transaction_log.initialize_daily_log()
        
        franchise_one = Franchise(1)
        franchise_two = Franchise(2)
        franchise_three = Franchise(3)

        franchise_one.place_order()
        franchise_three.place_order()
        franchise_one.place_order()
        franchise_two.place_order()
        franchise_three.place_order()
        franchise_two.place_order()