import argparse
import sys


def make_print_pairs_of(n):
    def print_pairs_of(*args):
        x = args
        for item1 in range(len(x)):
            for item2 in range(item1 + 1, len(x)):
                if x[item1] + x[item2] == n:
                    print(f'{x[item1]}+{x[item2]}')

    return print_pairs_of


def main():
    print_pairs = make_print_pairs_of(10)
    print_pairs(1, 2, 3, 4, 5, 5, 6)


if __name__ == '__main__':
    main()
