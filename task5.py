msg_info = 'To convert an integer to uppercase enter it: '
msg_error = "no integer was entered. You should enter an integer."


class NumberInWords:
    numbers = {
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

    def __init__(self, number):
        self.number = number

    def add_rank_hundred(self, number_in_words, value_rank):
        number_in_words.append(self.numbers[value_rank])
        number_in_words.append(self.numbers[100])

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

    def get_num_in_words(self):
        if self.num == 0:
            return self.numbers[0]
        ranks = self.get_ranks()
        len_ranks = len(ranks)
        number_in_words = []
        if self.num < 0:
            number_in_words.append('minus')
        for item in range(len_ranks):
            rank_hundreds = ranks[item] // 100
            if rank_hundreds != 0:
                self.add_rank_hundred(number_in_words, rank_hundreds)
            rank_tens = ranks[item] % 100
            if rank_tens != 0:
                if rank_tens < 21:
                    number_in_words.append(self.numbers[rank_tens])
                else:
                    number_in_words.append(self.numbers[rank_tens // 10 * 10])
                    number_in_words.append(self.numbers[rank_tens % 10])
            number_in_words.append(self.triads[len_ranks - 1 - item])
        numeric_line = ' '.join(number_in_words)
        return numeric_line


def main():
    try:
        number = int(input(msg_info))
        number = NumberInWords(number)
        print(number.get_num_in_words())
    except ValueError:
        print(msg_error)


if __name__ == '__main__':
    main()
