class ConsoleDisplay:
    @staticmethod
    def display_franchise_welcome(franchise_number):
        print(f'\nWelcome to the restaurant! This is franchise number {franchise_number}')

    @staticmethod
    def get_valid_user_order_type(order_options):
        options = ConsoleDisplay.configure_order_options(order_options)
        ConsoleDisplay.display_order_options(options)
        validated_input = (False, None)
        while validated_input[0] is False:
            user_input = input('To place an order, please enter the number of your menu selection: ')
            validated_input = ConsoleDisplay.validate_option_input(user_input, options)
        return validated_input[1]

    @staticmethod
    def configure_order_options(order_options):
        options = {}
        for index, option in enumerate(order_options):
            options[str(index + 1)] = (True, option)
        return options

    @staticmethod
    def display_order_options(options):
        print('\nBelow are the current menu options:')
        for key, option_tuple in options.items():
            print(f'{key} - {option_tuple[1].title()}')

    @staticmethod
    def validate_option_input(user_input, options):
        return options.get(user_input, (False, None))