from Validation import Validation

msg_next = 'To process the next pair of envelopes print "yes"/"y"'
msg_info = 'Parameters of envelopes must be positive numbers. The program determines whether one envelope can be ' \
           'nested inside another. Please, enter envelope parameters.'
msg_result_first_in_second = 'The first envelope fits into the second.'
msg_result_second_in_first = 'The second envelope fits into the first.'
msg_result_none = "No envelope fits inside another."


class Envelope:
    def __init__(self, length, width):
        self.length = max(length, width)
        self.width = min(length, width)


def env_compare(envelope1, envelope2):
    if envelope1.length > envelope2.length:
        message = msg_result_second_in_first if envelope1.width > envelope2.width else msg_result_none
    else:
        message = msg_result_first_in_second if envelope1.width < envelope2.width else msg_result_none
    return message


def main():
    while True:
        try:
            length1 = Validation.positive_float_validation(input('Enter a:'))
            width1 = Validation.positive_float_validation(input('Enter b:'))
            length2 = Validation.positive_float_validation(input('Enter c:'))
            width2 = Validation.positive_float_validation(input('Enter d:'))
        except ValueError:
            print(msg_info)
            continue
        env1 = Envelope(length1, width1)
        env2 = Envelope(length2, width2)
        print(env_compare(env1, env2))
        answer_next = input(msg_next).lower()
        if answer_next != 'yes' and answer_next != 'y':
            break


if __name__ == '__main__':
    main()
