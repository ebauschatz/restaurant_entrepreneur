"""Class file for console display and user input

Any message that is displayed to the user, including input prompts
should be contained in this class.
"""
class ConsoleDisplay:
    """Static class containing all display and input methods

    Public Static Methods:
        display_franchise_welcome(int) -> void
            Displays a welcome message for the chain and the franchise number
        get_valid_user_order_type(list: str) -> str
            Takes in a list of order type option strings and returns one selected by the user
        configure_order_options(list: str) - > dict
            Converts the list of order type option strings to a dictionary
        display_order_options(dict) -> void
            Displays all options from the order type option dictionary
        validate_option_input(str, dict) -> tuple
            Validates that the user selection is part of the dictionary of options
            If it is, it will return (True, option), else (False, None)
    """
    @staticmethod
    def display_franchise_welcome(franchise_number):
        """Displays a welcome message for the chain and the franchise number

        Effects:
            The restaurant chain name and franchise number are displayed to the console
        """
        print(f'\nWelcome to the Restaurant At the End of the World! This is franchise number {franchise_number}')

    @staticmethod
    def get_valid_user_order_type(order_options):
        """Takes in a list of order type option strings and returns one selected by the user

        Args:
            order_options: str
                a list of string representing the available order types
                these types will also appear in the OrderFactory class

        Effects:
            Will prompt user to enter the option to select via console input until they make a valid selection

        Returns:
            A string representing the value from the order options chosen by the user
        """
        options = ConsoleDisplay.configure_order_options(order_options)
        ConsoleDisplay.display_order_options(options)
        validated_input = (False, None)
        while validated_input[0] is False:
            user_input = input('To place an order, please enter the number of your menu selection: ')
            validated_input = ConsoleDisplay.validate_option_input(user_input, options)
        return validated_input[1]

    @staticmethod
    def configure_order_options(order_options):
        """Converts a list of strings to a dictionary

        Args:
            order_options: list(str)
                a list of strings representing the avaialble order options
                these options will also appear in the OrderFactory class

        Returns:
            A dictionary created from the list:
                key - the index of the element in the list plus one
                value - a tuple containing True and the value of the list element
        """
        options = {}
        for index, option in enumerate(order_options):
            options[str(index + 1)] = (True, option)
        return options

    @staticmethod
    def display_order_options(options):
        """Displays all available order type options

        Args:
            options: dict
                A dictionary representing all available order options
                    key - the option number
                    value - a tuple containing True and the option value (str)

        Effects:
            Prints all available option keys and option string values to the console
        """
        print('Below are the current menu options:')
        for key, option_tuple in options.items():
            print(f'{key} - {option_tuple[1].title()}')

    @staticmethod
    def validate_option_input(user_input, options):
        """Validates that the user selected a valid option from the list

        Args:
            user_input: str
                the value entered by the user
            options: dict
                a dictionary containing valid options
                the user input should correspond to a dictionary key

        Returns:
            A tuple containing True and the string value of the option selected if the
            user input was within the given options, or (False, None) if they made an invalid selection
        """
        return options.get(user_input, (False, None))