import argparse
import sys

from Validation import Validation

msg_info = 'To output natural numbers row whose square is less than given: '
msg_error = "No integer was entered. You should enter an integer."


class NumbersRow:
    """
    The main task of this class is to o output natural numbers row whose square is less than given.
    """

    def __init__(self, number_range):
        self.number_range = number_range

    # modified str method to show a comma separated string of numbers
    def __repr__(self):
        return ', '.join([str(n) for n in range(self.number_range) if -1 < n ** 2 < self.number_range])


def main():
    try:
        parser = argparse.ArgumentParser(description='Output natural numbers row')
        parser.add_argument('number_range', type=Validation.positive_integer_validation,
                            help='range for numbers whose square is less than given')
        args = parser.parse_args()
        print(NumbersRow(args.number_range))
    except ValueError:
        exc = sys.exc_info()[1]
        print(f'Use positive integer, instead of: {exc}')


if __name__ == '__main__':
    main()
