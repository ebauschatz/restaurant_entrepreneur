"""Class file for the overall restaurant simulation

Creates franchises and controls placement of orders
"""
from data_models.franchise import Franchise
from data_models.logger import transaction_log

class Simulation:
    """Represents the overall restaurant simulation

    Public Methods:
        run_simulation() -> void
            Runs the restaurant simulation
    """
    def run_simulation(self):
        """Runs the restaurant simulation

        Effects:
            Creates franchise instances and places multiple orders at each
        """
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