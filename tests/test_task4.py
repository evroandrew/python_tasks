import unittest
import task4
from unittest.mock import patch, mock_open


class TestFileParser(unittest.TestCase):
    """
    This class tests task4.py
    """

    def test_replace_line(self):
        self.assertEqual(task4.DataParser('text', 't', 'a').replace_line(), 'aexa')
        self.assertEqual(task4.DataParser('text', 'e', 'a').replace_line(), 'taxt')
        self.assertEqual(task4.DataParser('text', 'x', 'a').replace_line(), 'teat')
        self.assertEqual(task4.DataParser('text', 'a', 'a').replace_line(), 'text')
        self.assertEqual(task4.DataParser('text', 't', '').replace_line(), 'ex')
        self.assertEqual(task4.DataParser('text', 'e', '').replace_line(), 'txt')
        self.assertEqual(task4.DataParser('text', 'x', '').replace_line(), 'tet')
        self.assertEqual(task4.DataParser('text', 'a', '').replace_line(), 'text')

    def test_count_line(self):
        self.assertEqual(task4.DataParser('text', 't').count_line(), 2)
        self.assertEqual(task4.DataParser('text', 'e').count_line(), 1)
        self.assertEqual(task4.DataParser('text', 'x').count_line(), 1)
        self.assertEqual(task4.DataParser('text', 'a').count_line(), 0)
        self.assertEqual(task4.DataParser('text', 't', 'a').count_line(), 2)
        self.assertEqual(task4.DataParser('text', 'e', 'a').count_line(), 1)
        self.assertEqual(task4.DataParser('text', 'x', 'a').count_line(), 1)
        self.assertEqual(task4.DataParser('text', 'a', 'a').count_line(), 0)


if __name__ == '__main__':
    unittest.main()
