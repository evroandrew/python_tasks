import unittest
import task1


class TestChessboard(unittest.TestCase):
    """
    This class tests task1.py
    """

    def test_show_board(self):
        self.assertEqual(task1.Chessboard(2, 2).show_board(), print('* \n *\n'))
        self.assertEqual(task1.Chessboard(1, 1).show_board(), print('*\n'))
        self.assertEqual(task1.Chessboard(3, 3).show_board(), print('* *\n * \n* *\n'))
        self.assertEqual(task1.Chessboard(2, 2, '1', '2').show_board(), print('12\n21\n'))
        self.assertEqual(task1.Chessboard(1, 1, '%', '$').show_board(), print('%\n'))
        self.assertEqual(task1.Chessboard(3, 3, '@', '!').show_board(), print('!@!\n@!@\n!@!\n'))

    def test_create_lines(self):
        self.assertEqual(task1.ChessboardGenerator().create_lines(2), (' *', '* '))
        self.assertEqual(task1.ChessboardGenerator().create_lines(1), (' ', '*'))
        self.assertEqual(task1.ChessboardGenerator().create_lines(3), (' * ', '* *'))
        self.assertEqual(task1.ChessboardGenerator('1', '2').create_lines(2), ('21', '12'))
        self.assertEqual(task1.ChessboardGenerator('%', '$').create_lines(1), ('$', '%'))
        self.assertEqual(task1.ChessboardGenerator('@', '!').create_lines(3), ('!@!', '@!@'))

    def test_create_board(self):
        self.assertEqual(task1.ChessboardGenerator().create_board(2, 2), '* \n *\n')
        self.assertEqual(task1.ChessboardGenerator().create_board(3, 3), '* *\n * \n* *\n')
        self.assertEqual(task1.ChessboardGenerator().create_board(1, 1), '*\n')
        self.assertEqual(task1.ChessboardGenerator('1', '2').create_board(2, 2), '12\n21\n')
        self.assertEqual(task1.ChessboardGenerator('%', '$').create_board(1, 1), '%\n')
        self.assertEqual(task1.ChessboardGenerator('@', '!').create_board(3, 3), '@!@\n!@!\n@!@\n')


if __name__ == '__main__':
    unittest.main()
