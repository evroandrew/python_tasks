import argparse
import sys

msg_info = 'To output Fibonacci numbers within the specified range, enter range: '
msg_error = "Use any numbers."


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


def main():
    try:
        parser = argparse.ArgumentParser(description='Output Fibonacci numbers within the specified range')
        parser.add_argument('a', nargs='?', type=float, help='argument a for specified range')
        parser.add_argument('b', nargs='?', type=float, help='argument b for specified range')
        args = parser.parse_args()
        if args.b is None:
            try:
                print(msg_info)
                a = 'abs'
                while a == 'abs':
                    try:
                        a = float(input('Enter first argument of range: '))
                    except ValueError:
                        exc = sys.exc_info()[1]
                        print(exc)
                        print('Use any numbers, instead of it.')
                b = 'abs'
                while b == 'abs':
                    try:
                        b = float(input('Enter second argument of range: '))
                    except ValueError:
                        exc = sys.exc_info()[1]
                        print(exc)
                        print('Use any numbers, instead of it.')
                print(RangeOfFibonacciNumbers(a, b))
            except ValueError:
                exc = sys.exc_info()[1]
                print(f'Use any numbers, instead of: {exc}')
        else:
            print(RangeOfFibonacciNumbers(args.a, args.b))
    except ValueError:
        exc = sys.exc_info()[1]
        print(f'Use any numbers, instead of: {exc}')


if __name__ == '__main__':
    main()
