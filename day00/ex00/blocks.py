
from sys import stdin, argv


def blocks(stream, nlines):
    while nlines > 0 and (line := stream.readline()):
        nlines -= 1
        line = line.strip()
        if len(line) == 32 and line.startswith('0' * 5) and line[5] != '0':
            print(line)


def main():
    help_message = 'incorrect arguments'

    match len(argv):
        case 1:
            nlines = 10
        case 2:
            try:
                nlines = int(argv[1])
                if nlines < 0:
                    raise ValueError
            except Exception:
                print(help_message)
                exit()
        case _:
            print(help_message)
            exit()

    blocks(stdin, nlines)


if __name__ == '__main__':
    main()
