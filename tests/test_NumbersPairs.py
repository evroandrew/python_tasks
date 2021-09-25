import unittest
import NumbersPairs


class TestNumbersPairs(unittest.TestCase):
    """
    This class tests NumbersPairs.py
    """

    def test_print_pairs(self):
        print_pairs = NumbersPairs.make_print_pairs_of(10)
        self.assertEqual(print_pairs(1, 2, 3, 4, 5, 5, 6), print('4+6\n5+5'))
        print_pairs = NumbersPairs.make_print_pairs_of(7)
        self.assertEqual(print_pairs(1, 2, 3, 4, 5, 5, 6), print('1+6\n2+5\n2+5\n3+4'))


if __name__ == '__main__':
    unittest.main()
