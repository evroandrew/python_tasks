import argparse

MSG_next = 'To process the next pair of envelopes print "yes"/"y"'
MSG_info = 'Parameters of envelopes must be positive numbers.'
MSG_result_first_in_second = 'The first envelope fits into the second.'
MSG_result_second_in_first = 'The second envelope fits into the first.'
MSG_result_none = "No envelope fits inside another."

class Envelope:
    def __init__(self, length, width):
        self.length = max(length, width)
        self.width = min(length, width)

def validation(value):
    value = float(value)
    if value < 0:
        raise ValueError
    return value

def Env_compare(env1, env2):
    if env1.length > env2.length:
        message = MSG_result_second_in_first if env1.width > env2.width else RESULT_NONE_MSG
    else:        
        message = MSG_result_first_in_second if env1.width < env2.width else RESULT_NONE_MSG
    return message

while True:
    try:
        length1 = validation(input('Enter a:'))
        width1 = validation(input('Enter b:'))
        length2 = validation(input('Enter c:'))
        width2 = validation(input('Enter d:'))
    except ValueError:
        print(MSG_info)
        continue
    env1 = Envelope(length1, width1)
    env2 = Envelope(length2, width2)
    print(Env_compare(env1, env2))
    answ_next = input(MSG_next).lower()
    if answ_next != 'yes' and answ_next != 'y':
        break