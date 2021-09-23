import unittest
import task4
from unittest.mock import patch, mock_open


class TestFileParser(unittest.TestCase):
    """
    This class tests task4.py
    """

    def test_replace_line(self):
        test_cases = [
            {'arguments': {'data': 'text', 'line_to_search': 't', 'line_replace': 'a'}, 'excepted_result': 'aexa'},
            {'arguments': {'data': 'text', 'line_to_search': 'e', 'line_replace': 'a'}, 'excepted_result': 'taxt'},
            {'arguments': {'data': 'text', 'line_to_search': 'x', 'line_replace': 'a'}, 'excepted_result': 'teat'},
            {'arguments': {'data': 'text', 'line_to_search': 'a', 'line_replace': 'a'}, 'excepted_result': 'text'},
            {'arguments': {'data': 'text', 'line_to_search': 't', 'line_replace': ''}, 'excepted_result': 'ex'},
            {'arguments': {'data': 'text', 'line_to_search': 'e', 'line_replace': ''}, 'excepted_result': 'txt'},
            {'arguments': {'data': 'text', 'line_to_search': 'x', 'line_replace': ''}, 'excepted_result': 'tet'},
            {'arguments': {'data': 'text', 'line_to_search': 'a', 'line_replace': ''}, 'excepted_result': 'text'},
            {'arguments': {'data': 'text', 'line_to_search': 't', 'line_replace': 'a', 'replace_count': 1},
             'excepted_result': 'aext'},
            {'arguments': {'data': 'texte', 'line_to_search': 'e', 'line_replace': 'a', 'replace_count': 1},
             'excepted_result': 'taxte'},
            {'arguments': {'data': 'textx', 'line_to_search': 'x', 'line_replace': 'a', 'replace_count': 1},
             'excepted_result': 'teatx'},
            {'arguments': {'data': 'text', 'line_to_search': 'a', 'line_replace': 'a', 'replace_count': 1},
             'excepted_result': 'text'},
            {'arguments': {'data': 'text', 'line_to_search': 't', 'line_replace': '', 'replace_count': 1},
             'excepted_result': 'ext'},
            {'arguments': {'data': 'texte', 'line_to_search': 'e', 'line_replace': '', 'replace_count': 1},
             'excepted_result': 'txte'},
            {'arguments': {'data': 'textx', 'line_to_search': 'x', 'line_replace': '', 'replace_count': 1},
             'excepted_result': 'tetx'}
        ]
        for test_case in test_cases:
            self.assertEqual(task4.DataParser(**test_case['arguments']).replace_line(), test_case['excepted_result'])

    def test_count_line(self):
        self.assertEqual(task4.DataParser('text', 't').count_line(), 2)
        self.assertEqual(task4.DataParser('text', 'e').count_line(), 1)
        self.assertEqual(task4.DataParser('text', 'x').count_line(), 1)
        self.assertEqual(task4.DataParser('text', 'a').count_line(), 0)
        self.assertEqual(task4.DataParser('text', 't', 'a').count_line(), 2)
        self.assertEqual(task4.DataParser('text', 'e', 'a').count_line(), 1)
        self.assertEqual(task4.DataParser('text', 'x', 'a').count_line(), 1)
        self.assertEqual(task4.DataParser('text', 'a', 'a').count_line(), 0)
        self.assertEqual(task4.DataParser('', 'a', 'a').count_line(), 0)


if __name__ == '__main__':
    unittest.main()
