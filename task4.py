import argparse
from Validation import Validation
from FileWorker import FileWorker

msg_info = 'To count the number of occurrences of a string in a text file press 1. To replace a string with another ' \
           'one in the file press 2. To exit enter any other value. '
msg_file_path = 'Enter file path: '
msg_line_count = 'Enter string to count:'
msg_line_replace = 'Enter string to replace:'
msg_line_search = 'Enter string to search:'


class FileParser:
    def __init__(self, file_path, line_to_search, line_replace='', replace_count=-1):
        self.file_worker = FileWorker(file_path)
        self.line_to_search = line_to_search
        self.line_replace = line_replace
        self.replace_count = replace_count

    def replace_line(self):
        data = self.file_worker.read_file()
        if data != '':
            if self.replace_count == -1:
                data = data.replace(self.line_to_search, self.line_replace)
            else:
                data = data.replace(
                    self.line_to_search, self.line_replace, self.replace_count)
            self.file_worker.write_file(data)
            print(f'The text {self.line_to_search} was replaced in the file.')
        else:
            print('File is empty.')

    def count_line(self):
        data = self.file_worker.read_file()
        if data != '':
            counter = data.count(self.line_to_search)
            if counter > 1:
                print(
                    f'The text {self.line_to_search} was found in the file {counter} times.')
            elif counter == 1:
                print(
                    f'The text {self.line_to_search} was found in the file {counter} time.')
            else:
                print(f'The text {self.line_to_search} was not found in the file.')
        else:
            print('File is empty.')


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
        FileParser(file_path, line_to_search).count_line()
    else:
        line_replace = input(msg_line_replace)
        FileParser(file_path, line_to_search, line_replace).replace_line()


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
            FileParser(args.file_path, args.line_search).count_line()
        else:
            FileParser(args.file_path, args.line_search, args.line_replace).replace_line()
    except ValueError:
        worker()


if __name__ == '__main__':
    main()
