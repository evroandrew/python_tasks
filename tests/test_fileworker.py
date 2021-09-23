import unittest
from FileWorker import FileWorker
from unittest.mock import patch, mock_open


class TestFileWorker(unittest.TestCase):
    """
    This class tests FileWorker.py
    """

    def test_read_file(self):
        with patch('builtins.open', mock_open(read_data='text')) as file_read:
            data = FileWorker('path').read_file()
            self.assertEqual(data, 'text')

    def test_read_file_by_line(self):
        with patch('builtins.open', mock_open(read_data='text')) as file_read:
            data = FileWorker('path').read_file_by_line()
            self.assertEqual(data, ['text'])

    def test_write_file(self):
        with patch('builtins.open', mock_open()) as file_write:
            FileWorker('test.txt').write_file('text')
            file_write.assert_called_with('test.txt', 'w')
            file_write().write.assert_called_with('text')


if __name__ == '__main__':
    unittest.main()
