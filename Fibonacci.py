import argparse
import sys

msg_info = 'It is function which prints desired count of Fibonacci numbers. Enter Argument: '
msg_error = "Use any numbers."


class Fibonacci:
    """
    The main task of this class is to print desired count of Fibonacci numbers.
    """

    def __init__(self, a):
        self.a = a

    # modified str method to show a comma separated string of numbers
    def __repr__(self):
        return ', '.join(str(x) for x in self.numbers())

    # generator that produces a number in a given range
    def numbers(self):
        result = []
        first_number, second_number = 0, 1
        counter = 0
        while counter < self.a:
            yield first_number
            first_number, second_number = second_number, first_number + second_number
            counter += 1


def main():
    try:
        parser = argparse.ArgumentParser(description='Output Fibonacci numbers within the specified range')
        parser.add_argument('a', nargs='?', type=int, help='argument a for specified range')
        args = parser.parse_args()
        if args.a is None:
            try:
                print(msg_info)
                a = 'abs'
                while a == 'abs':
                    try:
                        a = int(input('Enter argument of range: '))
                    except ValueError:
                        exc = sys.exc_info()[1]
                        print(exc)
                        print('Use any numbers, instead of it.')
                print(Fibonacci(a))
            except ValueError:
                exc = sys.exc_info()[1]
                print(f'Use any numbers, instead of: {exc}')
        else:
            print(Fibonacci(args.a))
    except ValueError:
        exc = sys.exc_info()[1]
        print(f'Use any numbers, instead of: {exc}')


if __name__ == '__main__':
    main()
