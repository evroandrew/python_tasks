import unittest
import task5


class TestNumberInWords(unittest.TestCase):
    """
    This class tests task5.py
    """

    def test_representation(self):
        self.assertEqual(str(task5.NumberInWords(0)), 'zero')
        self.assertEqual(str(task5.NumberInWords(1)), 'one')
        self.assertEqual(str(task5.NumberInWords(250)), 'two hundred fifty')
        self.assertEqual(str(task5.NumberInWords(200)), 'two hundred')
        self.assertEqual(str(task5.NumberInWords(-234)), 'minus two hundred thirty four')
        self.assertEqual(str(task5.NumberInWords(-234981)),
                         'minus two hundred thirty four thousand nine hundred eighty one')
        self.assertEqual(str(task5.NumberInWords(0, 'ru')), 'ноль')
        self.assertEqual(str(task5.NumberInWords(1, 'ru')), 'один')
        self.assertEqual(str(task5.NumberInWords(250, 'ru')), 'двести пятьдесят')
        self.assertEqual(str(task5.NumberInWords(-234, 'ru')), 'минус двести тридцать четыре')
        self.assertEqual(str(task5.NumberInWords(-234981, 'ru')),
                         'минус двести тридцать четыре тысячи девятьсот восемьдесят один')
        self.assertEqual(str(task5.NumberInWords(0, 'en')), 'zero')
        self.assertEqual(str(task5.NumberInWords(1, 'en')), 'one')
        self.assertEqual(str(task5.NumberInWords(250, 'en')), 'two hundred fifty')
        self.assertEqual(str(task5.NumberInWords(200, 'en')), 'two hundred')
        self.assertEqual(str(task5.NumberInWords(-234, 'en')), 'minus two hundred thirty four')
        self.assertEqual(str(task5.NumberInWords(-234981, 'en')),
                         'minus two hundred thirty four thousand nine hundred eighty one')

    def test_get_ranks(self):
        first_number = task5.NumberInWords(595)
        self.assertEqual(first_number.get_ranks(), [595])
        second_number = task5.NumberInWords(595150)
        self.assertEqual(second_number.get_ranks(), [595, 150])
        third_number = task5.NumberInWords(595150200)
        self.assertEqual(third_number.get_ranks(), [595, 150, 200])

    def test_generate_hundred_in_words(self):
        self.assertEqual(task5.NumberInWords().generate_hundred_in_words(500), 'five hundred')
        self.assertEqual(task5.NumberInWords().generate_hundred_in_words(300), 'three hundred')
        self.assertEqual(task5.NumberInWords().generate_hundred_in_words(200), 'two hundred')
        self.assertEqual(task5.NumberInWords(0, 'ru').generate_hundred_in_words(500), 'пятьсот')
        self.assertEqual(task5.NumberInWords(0, 'ru').generate_hundred_in_words(300), 'триста')
        self.assertEqual(task5.NumberInWords(0, 'ru').generate_hundred_in_words(200), 'двести')

    def test_generate_units_in_words(self):
        self.assertEqual(task5.NumberInWords().generate_units_in_words(9), 'nine')
        self.assertEqual(task5.NumberInWords().generate_units_in_words(13), 'thirteen')
        self.assertEqual(task5.NumberInWords().generate_units_in_words(42), 'forty two')
        self.assertEqual(task5.NumberInWords(0, 'ru').generate_units_in_words(9), 'девять')
        self.assertEqual(task5.NumberInWords(0, 'ru').generate_units_in_words(13), 'тринадцать')
        self.assertEqual(task5.NumberInWords(0, 'ru').generate_units_in_words(42), 'сорок два')

    def test_generate_triad_in_words(self):
        self.assertEqual(task5.NumberInWords().generate_triad_in_words(2, 0, [234, 981]), 'thousand')
        self.assertEqual(task5.NumberInWords().generate_triad_in_words(1, 0, [234]), '')
        self.assertEqual(task5.NumberInWords().generate_triad_in_words(3, 1, [234, 000, 981]), '')
        self.assertEqual(task5.NumberInWords(0, 'ru').generate_triad_in_words(2, 0, [234, 981]), 'тысячи')
        self.assertEqual(task5.NumberInWords(0, 'ru').generate_triad_in_words(1, 0, [234]), '')
        self.assertEqual(task5.NumberInWords(0, 'ru').generate_triad_in_words(3, 1, [234, 000, 981]), '')


if __name__ == '__main__':
    unittest.main()
