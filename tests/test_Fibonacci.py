import unittest
import Fibonacci


class TestFibonacci(unittest.TestCase):
    """
    This class tests Fibonacci.py
    """

    def test_representation(self):
        self.assertEqual(str(Fibonacci.Fibonacci(10)), '0, 1, 1, 2, 3, 5, 8, 13, 21, 34')
        self.assertEqual(str(Fibonacci.Fibonacci(20)),
                         '0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181')
        self.assertEqual(str(Fibonacci.Fibonacci(1)), '0')
        self.assertEqual(str(Fibonacci.Fibonacci(0)), '')

    def test_numbers(self):
        self.assertEqual(list(Fibonacci.Fibonacci(10).numbers()), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(list(Fibonacci.Fibonacci(20).numbers()),
                         [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181])
        self.assertEqual(list(Fibonacci.Fibonacci(1).numbers()), [0])
        self.assertEqual(list(Fibonacci.Fibonacci(0).numbers()), [])


if __name__ == '__main__':
    unittest.main()
