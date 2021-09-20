import unittest
import task7


class TestNumbersRow(unittest.TestCase):
    """
    This class tests task7.py
    """

    def test_representation(self):
        self.assertEqual(str(task7.NumbersRow(1)), '0')
        self.assertEqual(str(task7.NumbersRow(100)), '0, 1, 2, 3, 4, 5, 6, 7, 8, 9')
        self.assertEqual(str(task7.NumbersRow(0)), '')
        self.assertEqual(str(task7.NumbersRow(-234981)), '')


if __name__ == '__main__':
    unittest.main()
