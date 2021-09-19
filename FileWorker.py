class FileWorker:
    msg_error = "File does not exist or access is denied. Please, try again."

    """
    The main task of this class is to work with file.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                data = file.read()
                return data
        except FileNotFoundError:
            print(self.msg_error)
            return ''

    def write_file(self, data):
        try:
            with open(self.file_path, 'w') as f:
                f.write(data)
        except FileNotFoundError:
            print(self.msg_error)
