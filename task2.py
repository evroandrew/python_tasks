import argparse

msg_next = 'To process the next pair of envelopes print "yes"/"y"'
msg_info = 'Parameters of envelopes must be positive numbers. The program determines whether one envelope can be nested inside another.'
msg_result_first_in_second = 'The first envelope fits into the second.'
msg_result_second_in_first = 'The second envelope fits into the first.'
msg_result_none = "No envelope fits inside another."

class Envelope:
    def __init__(self, length, width):
        self.length = max(length, width)
        self.width = min(length, width)

def validation(value):
    value = float(value)
    if value < 0:
        raise ValueError
    return value

def env_compare(env1, env2):
    if env1.length > env2.length:
        message = msg_result_second_in_first if env1.width > env2.width else msg_result_none
    else:        
        message = msg_result_first_in_second if env1.width < env2.width else msg_result_none
    return message

while True:
    try:
        length1 = validation(input('Enter a:'))
        width1 = validation(input('Enter b:'))
        length2 = validation(input('Enter c:'))
        width2 = validation(input('Enter d:'))
    except ValueError:
        print(msg_info)
        continue
    env1 = Envelope(length1, width1)
    env2 = Envelope(length2, width2)
    print(env_compare(env1, env2))
    answ_next = input(msg_next).lower()
    if answ_next != 'yes' and answ_next != 'y':
        break