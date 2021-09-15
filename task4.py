import argparse
msg_info = 'To count the number of occurrences of a string in a text file press 1. To replace a string with another one in the file press 2. To exit enter any other value.'
msg_file_path = 'Enter file path: '
msg_line_count = 'Enter string to count:'
msg_line_replace = 'Enter string to replace:'
msg_line_search = 'Enter string to search:'
msg_error = "File does not exist or access is denied. Please, try again."


class FileWorker:
    def __init__(self, file_path, line_serach, line_replace='', replace_count=-1):
        self.file_path = file_path
        self.line_serach = line_serach
        self.line_replace = line_replace
        self.replace_count = replace_count

    def replace_line(self):
        data = self.read_file()
        if self.replace_count == -1:
            data = data.replace(self.line_serach, self.line_replace)
        else:
            data = data.replace(
                self.line_serach, self.line_replace, self.replace_count)
        self.write_file(data)
        print(f'The text {self.line_serach} was replaced in the file.')

    def write_file(self, data):
        try:
            with open(self.file_path, 'w') as file:
                file.write(data)
        except FileNotFoundError:
            print(msg_error)

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file: 
                data = file.read()
                return data
        except FileNotFoundError:
            print(msg_error)
            return 42

    def count_line(self):
        data = self.read_file()
        if data!= 42:
            counter = data.count(self.line_serach)
            if counter > 1:
                print(
                    f'The text {self.line_serach} was found in the file {counter} times.')
            elif counter == 1:
                print(
                    f'The text {self.line_serach} was found in the file {counter} time.')
            else:
                print(f'The text {self.line_serach} was not found in the file.')


def input_validation(text):
    if text == '':
        print('You entered empty line')
        return True
    return False

def validation(value):
    if value =='':
        raise ValueError
    return value

def worker():
    choice = input(msg_info)
    if choice != '1' and choice != '2':
        return
    if choice == '1':
        file_path = input(msg_file_path)
        if input_validation(file_path):
            worker()
        line_serach = input(msg_line_count)
        if input_validation(line_serach):
            worker()
        file = FileWorker(file_path, line_serach)
        file.count_line()
    else:
        file_path = input(msg_file_path)
        if input_validation(file_path):
            worker()
        line_serach = input(msg_line_search)
        if input_validation(line_serach):
            worker()
        line_replace = input(msg_line_replace)
        file = FileWorker(file_path, line_serach, line_replace)
        file.replace_line()

try:
    parser = argparse.ArgumentParser(
        description='Enter arguments - file path, and text for count or text to search and text to replace')
    parser.add_argument('file_path',nargs='?', default =42, type=validation, help='file path')
    parser.add_argument('line_serach', nargs='?', default =42,type=validation, help='line serach')
    parser.add_argument('line_replace', nargs='?', default =42, help='line replace')
    args = parser.parse_args()
    if args.file_path==42 or args.line_serach==42:
        raise SystemExit
    if args.line_replace == 42:
        file = FileWorker(args.file_path, args.line_serach)
        file.count_line()
    else:
        file = FileWorker(args.file_path, args.line_serach, args.line_replace)
        file.replace_line()
except SystemExit:
    worker()