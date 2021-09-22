import argparse
from Validation import Validation
from FileWorker import FileWorker

msg_info = 'To count the number of occurrences of a string in a text file press 1. To replace a string with another ' \
           'one in the file press 2. To exit enter any other value. '
msg_file_path = 'Enter file path: '
msg_line_count = 'Enter string to count:'
msg_line_replace = 'Enter string to replace:'
msg_line_search = 'Enter string to search:'


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
    choice = input(msg_info)
    if choice != '1' and choice != '2':
        return
    file_path = input(msg_file_path)
    if Validation.string_is_empty(file_path):
        worker()
    line_to_search = input(msg_line_count)
    if Validation.string_is_empty(line_to_search):
        worker()
    if choice == '1':
        data = FileWorker(file_path).read_file()
        DataParser(data, line_to_search).count_line()
    else:
        line_replace = input(msg_line_replace)
        data = FileWorker(file_path).read_file()
        new_data = DataParser(data, line_to_search, line_replace).replace_line()
        if new_data != '':
            FileWorker(file_path).write_file(new_data)


def main():
    try:
        parser = argparse.ArgumentParser(
            description='Enter arguments - file path, and text for count or text to search and text to replace')
        parser.add_argument('file_path', nargs='?', default='', type=Validation.string_validation, help='file path')
        parser.add_argument('line_search', nargs='?', default='', type=Validation.string_validation,
                            help='line to search')
        parser.add_argument('line_replace', nargs='?', default=42, help='line replace')
        args = parser.parse_args()
        if args.file_path == '' or args.line_search == '':
            raise ValueError
        if args.line_replace == 42:
            data = FileWorker(args.file_path).read_file()
            DataParser(data, args.line_search).count_line()
        else:
            data = FileWorker(args.file_path).read_file()
            new_data = DataParser(data, args.line_search, args.line_replace).replace_line()
            if new_data != '':
                FileWorker(args.file_path).write_file(new_data)
    except ValueError:
        worker()


if __name__ == '__main__':
    main()
