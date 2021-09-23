import unittest
import task1


class TestChessboard(unittest.TestCase):
    """
    This class tests task1.py
    """

    def test_show_board(self):
        test_cases = [
            {'arguments': {'rows': 2, 'cols': 2}, 'excepted_result': print('* \n *\n')},
            {'arguments': {'rows': 1, 'cols': 1}, 'excepted_result': print('*\n')},
            {'arguments': {'rows': 3, 'cols': 3}, 'excepted_result': print('* *\n * \n* *\n')},
            {'arguments': {'rows': 2, 'cols': 2, 'cell1': '1', 'cell2': '2'}, 'excepted_result': print('12\n21\n')},
            {'arguments': {'rows': 1, 'cols': 1, 'cell1': '%', 'cell2': '$'}, 'excepted_result': print('%\n')},
            {'arguments': {'rows': 3, 'cols': 3, 'cell1': '@', 'cell2': '!'},
             'excepted_result': print('!@!\n@!@\n!@!\n')},
        ]
        for test_case in test_cases:
            self.assertEqual(task1.Chessboard(**test_case['arguments']).show_board(), test_case['excepted_result'])

    def test_create_lines(self):
        test_cases = [
            {'arguments1': {'cols': 2}, 'arguments0': {}, 'excepted_result': (' *', '* ')},
            {'arguments1': {'cols': 1}, 'arguments0': {}, 'excepted_result': (' ', '*')},
            {'arguments1': {'cols': 3}, 'arguments0': {}, 'excepted_result': (' * ', '* *')},
            {'arguments1': {'cols': 2}, 'arguments0': {'cell1': '1', 'cell2': '2'}, 'excepted_result': ('21', '12')},
            {'arguments1': {'cols': 1}, 'arguments0': {'cell1': '%', 'cell2': '$'}, 'excepted_result': ('$', '%')},
            {'arguments1': {'cols': 3}, 'arguments0': {'cell1': '@', 'cell2': '!'}, 'excepted_result': ('!@!', '@!@')},
        ]
        for test_case in test_cases:
            self.assertEqual(
                task1.ChessboardGenerator(**test_case['arguments0']).create_lines(**test_case['arguments1']),
                test_case['excepted_result'])

    def test_create_board(self):
        test_cases = [
            {'arguments1': {'cols': 2, 'rows': 2}, 'arguments0': {}, 'excepted_result': '* \n *\n'},
            {'arguments1': {'cols': 3, 'rows': 3}, 'arguments0': {}, 'excepted_result': '* *\n * \n* *\n'},
            {'arguments1': {'cols': 1, 'rows': 1}, 'arguments0': {}, 'excepted_result': '*\n'},
            {'arguments1': {'cols': 2, 'rows': 2}, 'arguments0': {'cell1': '1', 'cell2': '2'},
             'excepted_result': '12\n21\n'},
            {'arguments1': {'cols': 1, 'rows': 1}, 'arguments0': {'cell1': '%', 'cell2': '$'},
             'excepted_result': '%\n'},
            {'arguments1': {'cols': 3, 'rows': 3}, 'arguments0': {'cell1': '@', 'cell2': '!'},
             'excepted_result': '@!@\n!@!\n@!@\n'},
        ]
        for test_case in test_cases:
            self.assertEqual(
                task1.ChessboardGenerator(**test_case['arguments0']).create_board(**test_case['arguments1']),
                test_case['excepted_result'])


if __name__ == '__main__':
    unittest.main()
