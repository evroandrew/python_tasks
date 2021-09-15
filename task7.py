import argparse
msg_info = 'To convert an integer to uppercase enter it: '
msg_error = "no integer was entered. You should enter an integer."

class NumbersRow:
    def __init__(self, number_range):
        self.number_range = number_range

    def __repr__(self):
        return ', '.join([str(n) for n in range(self.number_range) if -1 < n**2 < self.number_range])

def validation(value):
    value = int(value)
    if value < 0:
        raise ValueError
    return value

try:
    parser = argparse.ArgumentParser(description='Output natural numbers row')
    parser.add_argument('number_range', type=validation, help='range for numbers whose square is less than given')
    args = parser.parse_args()    
    print(NumbersRow(args.number_range))
except argparse.ArgumentError:
    exc = sys.exc_info()[1]
    print(f'Use positive integer, instead of: {exc}')