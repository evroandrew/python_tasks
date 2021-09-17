import argparse
from Validation import Validation

msg_info = "In this program we can create a chessboard. For this you should enter two positive integers."


class Chessboard:
    """
    The main purpose of this class is to show a chessboard with two parameters:
    rows - int, basically 0,
    cols - int, basically 0.
    """

    def __init__(self, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.show_board()

    def show_board(self, el='*', cell=' '):
        chessboard = ChessboardGenerator(
            el, cell).create_board(self.rows, self.cols)
        print(chessboard)


class ChessboardGenerator:
    def __init__(self, el='*', cell=' '):
        self.el = el
        self.cell = cell
        self.new_line = '\n'

    def create_lines(self, cols):
        cols_range = cols // 2
        if cols % 2 == 1:
            cols_range += 1
        even_line = (self.el.join([f'{self.cell}' for col in range(cols_range)]))
        odd_line = (self.cell.join([f'{self.el}' for col in range(cols_range)]))
        if cols % 2 == 0:
            even_line += self.el
            odd_line += self.cell
        return odd_line, even_line

    def create_board(self, rows, cols):
        odd_line, even_line = self.create_lines(cols)
        chessboard = ''
        for row in range(rows):
            if row % 2 == 1:
                chessboard = f"{chessboard}{odd_line}{self.new_line}"
            else:
                chessboard = f"{chessboard}{even_line}{self.new_line}"
        return chessboard


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description='Enter two arguments - rows and cols for chessboard')
        parser.add_argument('rows', type=Validation.positive_integer_validation, help='Rows number')
        parser.add_argument('cols', type=Validation.positive_integer_validation, help='Cols number')
        args = parser.parse_args()
        chessboard = Chessboard(args.rows, args.cols)
    except SystemExit:
        print(msg_info)
