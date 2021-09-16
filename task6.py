class LuckyTickets:
    def __init__(self, func_chose):
        def lucky_moscow(ticket):
            return sum(map(int, ticket[:3])) == sum(map(int, ticket[3:]))

        def lucky_piter(ticket):
            return sum([int(ticket[i]) for i in range(6) if i % 2 == 0]) == \
                   sum([int(ticket[i]) for i in range(6) if i % 2 != 0])

        self.func_chose = func_chose
        self.lucky_validation = {0: lucky_moscow,
                                 1: lucky_piter}

    def is_lucky(self, ticket):
        return self.lucky_validation[self.func_chose](ticket)

    @property
    def number_of_lucky_tickets(self):
        lucky_tickets = []
        for i in range(1, 1000000):
            ticket = f'{i:06}'
            if self.is_lucky(ticket):
                lucky_tickets.append(ticket)
        return len(lucky_tickets)

    @property
    def lucky_tickets(self):
        specified_method = 'Moscow' if self.func_chose == 0 else 'Piter'
        rep = f'Number of lucky tickets for the {specified_method} method is {self.number_of_lucky_tickets}.'
        return rep


msg_file_path = 'Enter file path: '
msg_info = 'Program counts number of lucky tickets. Please, enter file path to chose counting algorithm.'
msg_error = "File does not exist or access is denied. Please, try again."


def path_validation(text):
    if text == '':
        print(msg_info)
        return False
    return True


def data_validation(data):
    if data != '':
        return True
    return False


def method_validation(data, methods):
    if data in methods:
        return True
    return False


class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                data = file.read()
                return data
        except FileNotFoundError:
            print(msg_error)
            return []


def main():
    file_path = input(msg_file_path)
    if path_validation(file_path):
        data = File(file_path).read_file()
        if data_validation(data):
            methods = {'Moscow': 0,
                       'Piter': 1}
            if method_validation(data, methods):
                print(LuckyTickets(methods[data]).lucky_tickets)
            else:
                print(msg_info)
        else:
            print(msg_info)
    else:
        print(msg_info)

if __name__ == '__main__':
    main()
