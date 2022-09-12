"""Main entry point for the program
"""
from data_models.simulation import Simulation

def main():
    """Main application entry point

    Effects:
        Runs the entire restaurant simulation
    """
    simulation = Simulation()
    simulation.run_simulation()


if __name__ == '__main__':
    main()