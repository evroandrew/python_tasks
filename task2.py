from _validator import Validator

MSG_NEXT = 'To process the next pair of envelopes print "yes"/"y"'
MSG_INFO = 'Parameters of envelopes must be positive numbers. The program determines whether one envelope can be ' \
           'nested inside another. Please, enter envelope parameters.'


class Envelope:
    """
    The main task of this class is to create envelopes.
    """

    def __init__(self, length, width):
        self.length = max(length, width)
        self.width = min(length, width)

    @staticmethod
    def env_compare(envelope1, envelope2):
        """
        envelope comparison method - check if one envelope fits into another
        """
        msg_result_none = "No envelope fits inside another."
        msg_result_first_in_second = 'The first envelope fits into the second.'
        msg_result_second_in_first = 'The second envelope fits into the first.'
        if envelope1.length == envelope2.length and envelope1.width == envelope2.width:
            return msg_result_none + " Envelope are the same."
        if envelope1.length > envelope2.length:
            message = msg_result_second_in_first if envelope1.width > envelope2.width else msg_result_none
        else:
            message = msg_result_first_in_second if envelope1.width < envelope2.width else msg_result_none
        return message


def main():
    while True:
        try:
            validation = Validator()
            length1 = validation.positive_float_validation(input('Enter a:'))
            width1 = validation.positive_float_validation(input('Enter b:'))
            length2 = validation.positive_float_validation(input('Enter c:'))
            width2 = validation.positive_float_validation(input('Enter d:'))
        except ValueError:
            print(MSG_INFO)
            continue
        env1 = Envelope(length1, width1)
        env2 = Envelope(length2, width2)
        print(Envelope.env_compare(env1, env2))
        answer_next = input(MSG_NEXT).lower()
        if answer_next not in ['yes', 'y']:
            break


if __name__ == '__main__':
    main()
