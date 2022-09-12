from data_models.franchise import Franchise

class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        franchise_one = Franchise(1)
        franchise_one.place_order()