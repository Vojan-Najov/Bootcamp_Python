#!/usr/bin/env python3

from sys import stdin


def mfinder():
    nlines = 0
    template = (
        '*   *',
        '** **', 
        '* * *',
    )
    isequal = True
    iserror = False

    while line := stdin.readline().strip():
        if len(line) != 5 or nlines > 2:
            iserror = True
        elif not iserror and isequal:
            isequal = all(
                template[nlines][i] == '*' == line[i] or
                template[nlines][i] != '*' != line[i]
                for i in range(5)
            )
        nlines += 1

    if iserror or nlines < 3:
        print('Error')
    else:
        print(isequal)


if __name__ == '__main__':
    mfinder()
