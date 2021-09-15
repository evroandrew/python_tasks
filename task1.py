import argparse

instructions = "In this program we can create a chessboard. For this you should enter two positive integers."

class Chessboard:
    def __init__(self, rows=None, cols=None):
        self.rows = rows
        self.cols = cols
        self.show_board()

    def show_board(self):
        chessboard = ChessboardGenerator().create_board(self.rows, self.cols)
        print(chessboard)

class ChessboardGenerator:    
    def __init__(self, el='*', cell=' '):
        self.el = el
        self.cell = cell        
        self.new_line = '\n'
    
    def create_board(self, rows, cols):        
        chessboard = ''        
        for row in range(rows):
            inner = []
            if row % 2 == 1:
                chessboard = f"{chessboard}{(''.join([f'{self.cell}{self.el}' for col in range(int(cols/2))]))}{self.new_line}"
            else:
                chessboard = f"{chessboard}{(self.cell.join([f'{self.el}' for col in range(int(cols/2))]))}{self.new_line}"
        return chessboard

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