from _fileworker import FileWorker


class LuckyTickets:
    """
    The main task of this class is to display number of lucky tickets with specified counting algorithm.
    """

    # method with moscow check
    @staticmethod
    def lucky_moscow(ticket):
        return sum(map(int, ticket[:3])) == sum(map(int, ticket[3:]))

    # method with piter check
    @staticmethod
    def lucky_piter(ticket):
        return sum([int(ticket[i]) for i in range(6) if i % 2 == 0]) == \
               sum([int(ticket[i]) for i in range(6) if i % 2 != 0])

    # method with piter check from task
    @staticmethod
    def lucky_piter_task(ticket):
        return sum([int(i) for i in ticket if int(i) % 2 == 0]) == \
               sum([int(i) for i in ticket if int(i) % 2 != 0])

    def __init__(self, func_chose='Moscow', tickets=[]):
        func_chose = func_chose
        lucky_validation = {'Moscow': self.lucky_moscow,
                            'Piter_alternative': self.lucky_piter,
                            'Piter': self.lucky_piter_task}

        specified_check = {'Moscow': 'Moscow',
                           'Piter_alternative': 'Piter',
                           'Piter': 'Piter task'}

        self.specified_method = specified_check[func_chose]
        self.lucky_validator = lucky_validation[func_chose]
        self.tickets = tickets

    # successful ticket method
    def is_lucky(self, ticket):
        return self.lucky_validator(ticket)

    @property
    def number_of_lucky_tickets(self):
        lucky_tickets = []
        for ticket in self.tickets:
            if self.is_lucky(ticket):
                lucky_tickets.append(ticket)
        return len(lucky_tickets)

    @property
    def lucky_tickets(self):
        rep = f'Number of lucky tickets for the {self.specified_method} method is {self.number_of_lucky_tickets}.'
        return rep


MSG_INFO = 'Program counts number of lucky tickets. Please, enter valid file path to chose counting algorithm.'


def main():
    try:
        file_path = input('Enter file path: ')
        if file_path != '':
            data = FileWorker(file_path).read_file_by_line()
            if data != '':
                methods = ['Moscow', 'Piter', 'Piter_alternative']
                if data[0] in methods:
                    tickets = []
                    for item in data:
                        if len(item) == 6 and item.isdigit():
                            tickets.append(item)
                    print(LuckyTickets(data[0], tickets).lucky_tickets)
                else:
                    print(MSG_INFO)
            else:
                print(MSG_INFO)
        else:
            print(MSG_INFO)
    except ValueError:
        print(MSG_INFO)


if __name__ == '__main__':
    main()
