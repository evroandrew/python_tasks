from Validation import Validation
from FileWorker import FileWorker


class LuckyTickets:
    """
    The main task of this class is to display number of lucky tickets with specified counting algorithm.
    """

    def __init__(self, func_chose, tickets):
        # method with moscow check
        def lucky_moscow(ticket):
            return sum(map(int, ticket[:3])) == sum(map(int, ticket[3:]))

        # method with piter check
        def lucky_piter(ticket):
            return sum([int(ticket[i]) for i in range(6) if i % 2 == 0]) == \
                   sum([int(ticket[i]) for i in range(6) if i % 2 != 0])

        # method with piter check from task
        def lucky_piter_task(ticket):
            return sum([int(i) for i in ticket if int(i) % 2 == 0]) == \
                   sum([int(i) for i in ticket if int(i) % 2 != 0])

        self.func_chose = func_chose
        self.tickets = tickets
        self.lucky_validation = {0: lucky_moscow,
                                 1: lucky_piter,
                                 2: lucky_piter_task}

        self.specified_check = {0: 'Moscow',
                                1: 'Piter',
                                2: 'Piter task'}

    # successful ticket method
    def is_lucky(self, ticket):
        return self.lucky_validation[self.func_chose](ticket)

    @property
    def number_of_lucky_tickets(self):
        lucky_tickets = []
        for ticket in self.tickets:
            if self.is_lucky(ticket):
                lucky_tickets.append(ticket)
        return len(lucky_tickets)

    @property
    def lucky_tickets(self):
        specified_method = self.specified_check[self.func_chose]
        rep = f'Number of lucky tickets for the {specified_method} method is {self.number_of_lucky_tickets}.'
        return rep


msg_file_path = 'Enter file path: '
msg_info = 'Program counts number of lucky tickets. Please, enter valid file path to chose counting algorithm.'


def main():
    try:
        file_path = input(msg_file_path)
        if not Validation.string_is_empty(file_path):
            data = FileWorker(file_path).read_file_by_line()
            if data != '':
                methods = {'Moscow': 0,
                           'Piter': 2,
                           'Piter_alternative': 1}
                if Validation.method_validation(data[0], methods):
                    tickets = Validation.tickets_validation(data)
                    print(LuckyTickets(methods[data[0]], tickets).lucky_tickets)
                else:
                    print(msg_info)
            else:
                print(msg_info)
        else:
            print(msg_info)
    except ValueError:
        print(msg_info)


if __name__ == '__main__':
    main()
