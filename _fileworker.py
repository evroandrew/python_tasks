class FileWorker:
    msg_file_not_found = "File does not exist. Please, try again."
    msg_permission = "Access is denied. Please, try again."

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
            print(self.msg_file_not_found)
            return ''
        except PermissionError:
            print(self.msg_permission)
            return ''

    def read_file_by_line(self):
        try:
            with open(self.file_path, 'r') as file:
                data = []
                for line in file:
                    data.append(line.strip())
                return data
        except FileNotFoundError:
            print(self.msg_file_not_found)
            return ''
        except PermissionError:
            print(self.msg_permission)
            return ''

    def write_file(self, data):
        try:
            with open(self.file_path, 'w') as f:
                f.write(data)
        except PermissionError:
            print(self.msg_permission)
