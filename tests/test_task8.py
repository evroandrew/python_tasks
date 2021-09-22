import unittest
import task8


class TestRangeOfFibonacciNumbers(unittest.TestCase):
    """
    This class tests task8.py
    """

    def test_representation(self):
        self.assertEqual(str(task8.RangeOfFibonacciNumbers(1, 10)), '2, 3, 5, 8')
        self.assertEqual(str(task8.RangeOfFibonacciNumbers(100, 200)), '144')
        self.assertEqual(str(task8.RangeOfFibonacciNumbers(0, 1)), '')
        self.assertEqual(str(task8.RangeOfFibonacciNumbers(-234981, 0)), '')

    def test_numbers(self):
        self.assertEqual(list(task8.RangeOfFibonacciNumbers(1, 10).numbers()), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(list(task8.RangeOfFibonacciNumbers(100, 200).numbers()),
                         [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])
        self.assertEqual(list(task8.RangeOfFibonacciNumbers(0, 1).numbers()), [0])
        self.assertEqual(list(task8.RangeOfFibonacciNumbers(-234981, 0).numbers()), [])


if __name__ == '__main__':
    unittest.main()