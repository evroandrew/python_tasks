msg_info = 'To convert an integer to uppercase enter it: '
msg_error = "no integer was entered. You should enter an integer."

NUMBERS = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
}
triads = ['', 'thousand', 'million', 'billion', 'trillion',
          'quadrillion', 'quintillion', 'sextillion']


class NumToWords:
    def __init__(self, num):
        self.num = num

    def get_num_to_words(self):
        val = abs(self.num)
        order = []
        while val/1000 > 1:
            order_value = val % 1000
            order.append(order_value)
            val = val//1000
        order.append(val)
        order.reverse()
        len_order = len(order)
        number = []
        if self.num < 0:
            number.append('minus')
        if val == 0:
            return NUMBERS[0]
        for item in range(len_order):
            val = order[item]
            val_order = val//100
            if val_order != 0:
                number.append(NUMBERS[val_order])
                number.append(NUMBERS[100])
            val_order = val % 100
            if val_order != 0:
                if val_order < 21:
                    number.append(NUMBERS[val_order])
                else:
                    number.append(NUMBERS[val_order//10*10])
                    number.append(NUMBERS[val_order % 10])
            number.append(triads[len_order-1-item])
        number = ' '.join(number)
        return number


try:
    number = input(msg_info)
    number = NumToWords(int(number))
except ValueError:
    print(msg_error)
print(number.get_num_to_words())