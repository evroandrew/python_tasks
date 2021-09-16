class Validation:
    def __init__(self):
        pass

    def positive_integer_validation(value):
        value = int(value)
        if value < 0:
            raise ValueError
        return value

    def positive_float_validation(value):
        value = float(value)
        if value < 0:
            raise ValueError
        return value

    def triangle_arguments_validation(args):
        if len(args) != 4:
            raise ValueError
        if any(float(side) < 0 for side in args[1:]):
            raise ValueError

    def string_is_empty(text):
        if text == '':
            print('You entered empty line')
            return True
        return False

    def string_validation(value):
        if value == '':
            raise ValueError
        return value

    def method_validation(data, methods):
        if data in methods:
            return True
        return False
