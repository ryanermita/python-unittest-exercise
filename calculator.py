class Calculator:
    """ A simple calculator App"""

    def add(x, y):
        """Add Function"""
        try:
            return x + y

        except TypeError as e:
            raise TypeError("Invalid Value")

    def subtract(x, y):
        """Subtract Function"""
        return x - y

    def multiply(x, y):
        """Multiply Function"""
        return x * y

    def divide(x, y):
        """Divide Function"""
        try:
            if y == 0:
                raise ValueError('Can not divide by zero!')

            return x / y

        except TypeError as e:
            raise TypeError("Invalid Value")
