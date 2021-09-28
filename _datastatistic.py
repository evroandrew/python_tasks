import re

msg_file_not_found = "File does not exist. Please, try again."
msg_permission = "Access is denied. Please, try again."


def data_statistic(file_path='data.txt', symbol='z', word='and'):
    try:
        with open(file_path, 'r') as file:
            data = []
            for line in file:
                data.append(line)
    except FileNotFoundError:
        print(msg_file_not_found)
        return ''
    except PermissionError:
        print(msg_permission)
        return ''
    counters = [0, 0, 0, 0, 0]
    for line in data:
        counters[0] += 1
        if line == '\n':
            counters[1] += 1
        if symbol in line:
            counters[2] += 1
        counters[3] += line.count(symbol)
        count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), line))
        if count > 0:
            counters[4] += 1
    print('Lines: ', counters[0])
    print('Empty lines: ', counters[1])
    print(f'Lines with "{symbol}": {counters[2]}')
    print(f'"{symbol}" count: {counters[3]}')
    print(f'Lines with "{word}": {counters[4]}')


def main():
    data_statistic()


if __name__ == '__main__':
    main()
