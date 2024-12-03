#!/usr/bin/env python3
from sys import argv


def decypher(string):
    return ''.join(word[0] for word in string.split()).capitalize()


def main():
    match len(argv):
        case 2:
            print(decypher(argv[1]))
        case _:
            print('incorrect arguments')


if __name__ == '__main__':
    main()

