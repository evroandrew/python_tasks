import argparse

MSG_INFO = 'To output Fibonacci numbers within the specified range, enter range: '


class RangeOfFibonacciNumbers:
    """
    The main task of this class is to output Fibonacci numbers within the specified range.
    """

    def __init__(self, a, b):
        self.a, self.b = sorted([a, b])

    # modified str method to show a comma separated string of numbers
    def __repr__(self):
        return ', '.join(str(x) for x in self.numbers() if self.a < x)

    # generator that produces a number in a given range
    def numbers(self):
        result = []
        first_number, second_number = 0, 1
        while first_number < self.b:
            yield first_number
            first_number, second_number = second_number, first_number + second_number


ERRORS = (argparse.ArgumentError, TypeError, argparse.ArgumentTypeError)


def main():
    try:
        parser = argparse.ArgumentParser(description='Output Fibonacci numbers within the specified range',
                                         exit_on_error=True)
        parser.add_argument('a', nargs='?', type=float, help='argument a for specified range')
        parser.add_argument('b', nargs='?', type=float, help='argument b for specified range')
        args = parser.parse_args()
        if args.b is None:
            try:
                print(MSG_INFO)
                a = 'abs'
                while a == 'abs':
                    try:
                        a = float(input('Enter first argument of range: '))
                    except ValueError as exc:
                        print(f'Use any numbers, instead of: {str(exc)}')
                b = 'abs'
                while b == 'abs':
                    try:
                        b = float(input('Enter second argument of range: '))
                    except ValueError as exc:
                        print(f'Use any numbers, instead of: {str(exc)}')
                print(RangeOfFibonacciNumbers(a, b))
            except ValueError as exc:
                print(f'Use any numbers, instead of: {str(exc)}')
        else:
            print(RangeOfFibonacciNumbers(args.a, args.b))
    except ERRORS as exc:
        print(f'Use any numbers, instead of: {str(exc)}')


if __name__ == '__main__':
    main()
