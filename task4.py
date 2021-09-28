import argparse
import pathlib
from _fileworker import FileWorker

MSG_INFO = 'To count the number of occurrences of a string in a text file press 1.\n' \
           'To replace a string with another one in the file press 2.\n' \
           'To exit enter any other value. '


class DataParser:
    """
    The main task of this class is to create file parser with functions for counting occurrences of a substring and
    replacing a string in a file.
    """

    def __init__(self, data, line_to_search, line_replace='', replace_count=-1):
        self.data = data
        self.line_to_search = line_to_search
        self.line_replace = line_replace
        self.replace_count = replace_count

    # Replace  line in a file
    def replace_line(self):
        if self.data != '':
            if self.replace_count == -1:
                data = self.data.replace(self.line_to_search, self.line_replace)
            else:
                data = self.data.replace(
                    self.line_to_search, self.line_replace, self.replace_count)
            print(f'The text {self.line_to_search} was replaced in the file.')
            return data
        else:
            print('File is empty.')
            return ''

    # Count the number of occurrences of a line in a text file
    def count_line(self):
        if self.data != '':
            counter = self.data.count(self.line_to_search)
            if counter > 1:
                print(
                    f'The text {self.line_to_search} was found in the file {counter} times.')
            elif counter == 1:
                print(
                    f'The text {self.line_to_search} was found in the file {counter} time.')
            else:
                print(f'The text {self.line_to_search} was not found in the file.')
            return counter
        else:
            print('File is empty.')
            return 0


# method of working with dialog code
def worker():
    msg_file_path = 'Enter file path: '
    msg_line_count = 'Enter string to count:'
    msg_line_replace = 'Enter string to replace:'
    choice = input(MSG_INFO)
    if choice != '1' and choice != '2':
        return
    file_path = input(msg_file_path)
    if file_path == '':
        print('You entered empty line')
        worker()
    line_to_search = input(msg_line_count)
    if line_to_search == '':
        print('You entered empty line')
        worker()
    if choice == '1':
        data = FileWorker(file_path).read_file()
        DataParser(data, line_to_search).count_line()
    else:
        line_replace = input(msg_line_replace)
        data = FileWorker(file_path).read_file()
        new_data = DataParser(data, line_to_search, line_replace).replace_line()
        FileWorker(file_path).write_file(new_data)


ERRORS = (argparse.ArgumentError, TypeError)


def main():
    try:
        parser = argparse.ArgumentParser(
            description='Enter arguments - file path, and text for count or text to search and text to replace',
            exit_on_error=False)
        parser.add_argument('file_path', nargs='?', type=pathlib.Path, help='file path')
        parser.add_argument('line_search', nargs='?', type=str, help='line to search')
        parser.add_argument('line_replace', nargs='?', type=str, default=42, help='line replace')
        args = parser.parse_args()
        if args.line_replace == 42:
            data = FileWorker(args.file_path).read_file()
            DataParser(data, args.line_search).count_line()
        else:
            data = FileWorker(args.file_path).read_file()
            new_data = DataParser(data, args.line_search, args.line_replace).replace_line()
            FileWorker(args.file_path).write_file(new_data)
    except ERRORS:
        worker()


if __name__ == '__main__':
    main()
