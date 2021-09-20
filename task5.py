msg_info = 'To convert an integer to uppercase enter it: '
msg_error = "no integer was entered. You should enter an integer."
msg_mode = 'To select the language to transform the number into, enter en or ru: '


class NumberInWords:
    """
    The main task of this class is to convert an integer to uppercase.
    """
    numbers_en = {
        -1: 'minus',
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
        100: 'hundred'
    }
    triads_en = ['', 'thousand', 'million', 'billion', 'trillion',
                 'quadrillion', 'quintillion', 'sextillion']
    numbers_ru = {
        -1: 'минус',
        0: 'ноль',
        1: ('один', 'одна'),
        2: ('два', 'две'),
        3: 'три',
        4: 'четыре',
        5: 'пять',
        6: 'шесть',
        7: 'семь',
        8: 'восем',
        9: 'девять',
        10: 'десять',
        11: 'одинадцать',
        12: 'двенадцать',
        13: 'тринадцать',
        14: 'четырнадцать',
        15: 'пятнадцать',
        16: 'шестнадцать',
        17: 'семнадцать',
        18: 'восемнадцать',
        19: 'девятнадцать',
        20: 'двадцать',
        30: 'тридцать',
        40: 'сорок',
        50: 'пятьдесят',
        60: 'шестьдесят',
        70: 'семьдесят',
        80: 'восемьдесят',
        90: 'девяносто',
        100: 'сто',
        200: 'двести',
        300: 'триста',
        400: 'четыреста',
        500: 'пятьсот',
        600: 'шестьсот',
        700: 'семьсот',
        800: 'восемьсот',
        900: 'девятьсот',
    }
    triads_ru = ['', ('тысяча', 'тысячи', 'тысяч'), ('миллион', 'миллиона', 'миллионов'),
                 ('биллион', 'биллиона', 'биллионов'), ('триллион', 'триллиона', 'триллионов'),
                 ('квадрилион', 'квадрилиона', 'квадрилионов'), ('квантилион', 'квантилиона', 'квантилионов'),
                 ('секстилион', 'секстилиона', 'секстилионов')]

    def __init__(self, number=0, mode='en'):
        self.mode = mode
        self.number = number
        if self.mode == 'en':
            self.numbers, self.triads = self.numbers_en, self.triads_en
        else:
            self.numbers, self.triads = self.numbers_ru, self.triads_ru

    # get hundreds in words
    def generate_hundred_in_words(self, rank_value):
        hundreds_value = rank_value // 100
        if hundreds_value == 0:
            return ''
        if self.mode == 'en':
            hundreds = self.numbers[hundreds_value], self.numbers[100]
            return ' '.join(hundreds)
        if self.mode == 'ru':
            return self.numbers[hundreds_value * 100]

    # get list of ranks
    def get_ranks(self):
        value = abs(self.number)
        ranks = []
        while value / 1000 > 1:
            rank_value = value % 1000
            ranks.append(rank_value)
            value = value // 1000
        ranks.append(value)
        ranks.reverse()
        return ranks

    # get tens and units in words
    def generate_units_in_words(self, rank_value):
        units = rank_value % 100
        if units != 0:
            if units < 21:
                if self.mode == 'ru' and (units == 1 or units == 2):
                    return self.numbers[units][0]
                else:
                    return self.numbers[units]
            else:
                words = [self.numbers[units // 10 * 10]]
                units = units % 10
                if units != 0:
                    if self.mode == 'ru' and (units == 1 or units == 2):
                        words.append(self.numbers[units][0])
                    else:
                        words.append(self.numbers[units])
                return ' '.join(words)
        return ''

    # modified str method to convert an integer to uppercase
    def __repr__(self):
        if self.number == 0:
            return self.numbers[0]
        number_in_words = []
        if self.number < 0:
            number_in_words.append(self.numbers[-1])
        ranks = self.get_ranks()
        number_of_ranks = len(ranks)
        for item in range(number_of_ranks):
            hundreds = self.generate_hundred_in_words(ranks[item])
            if hundreds != '':
                number_in_words.append(hundreds)
            units = self.generate_units_in_words(ranks[item])
            if units != '':
                number_in_words.append(units)
            if self.triads[number_of_ranks - 1 - item] != '':
                triad = self.triads[number_of_ranks - 1 - item]
                if self.mode == 'en':
                    number_in_words.append(triad)
                else:
                    triad_word = ranks[item] % 10
                    if triad_word == 0 or triad_word > 4:
                        triad_word = 2
                    elif triad_word != 1:
                        triad_word = 1
                    number_in_words.append(triad[triad_word])
        numeric_line = ' '.join(number_in_words)
        return numeric_line


def main():
    try:
        number = int(input(msg_info))
        mode = str(input(msg_mode))
        if mode in ['en', 'ru']:
            print(NumberInWords(number, mode))
        else:
            print(NumberInWords(number))
    except ValueError:
        print(msg_error)


if __name__ == '__main__':
    main()
