class Validation:
    """
    The main task of this class is to validate data.
    """

    @staticmethod
    def positive_integer_validation(value):
        value = int(value)
        if value < 0:
            raise ValueError
        return value

    @staticmethod
    def positive_float_validation(value):
        value = float(value)
        if value <= 0:
            raise ValueError
        return value
