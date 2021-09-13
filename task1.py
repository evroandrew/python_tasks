import argparse

instructions = "In this program we can create a chessboard. For this you should enter two positive integers."

class Chessboard:
    def __init__(self, rows=None, cols=None):
        self.rows = rows
        self.cols = cols
        self.show_board()

    def create_board(self):
        chessboard = ''
        for row in range(self.rows):
            inner = []
            for col in range(int(self.cols/2)):
                inner.append('*')
            new_line = '\n'
            if row % 2 == 1:
                chessboard = f"{chessboard}{(''.join([f' {el}' for el in inner]))}{new_line}"
            else:
                chessboard = f"{chessboard}{(' '.join([f'{el}' for el in inner]))}{new_line}"
        return chessboard

    def show_board(self):
        chessboard = self.create_board()
        print(chessboard)

def validation(value):
    value = int(value)
    if value < 0:
        raise ValueError
    return value

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description='Enter two arguments - rows and cols for chessboard')
        parser.add_argument('rows', type=validation, help='Rows number')
        parser.add_argument('cols', type=validation, help='Cols number')
        args = parser.parse_args()
        Chessboard(args.rows, args.cols)
    except SystemExit:
        print(instructions)