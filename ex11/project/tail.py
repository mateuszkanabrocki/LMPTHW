#! /usr/bin/env python3

from sys import argv
from sys import exit
# history | ./tail -25


def arguments(argv):
    try:
        lines_num = int(argv[1].strip('-'))
        return lines_num
    except:
        exit(1)


def standin():
    text = []
    while True:
        try:
            text.append(input())
        except EOFError:
            break
    return text


def main():
    count = arguments(argv)
    in_lines = standin()

    out_lines = []
    for line in in_lines[-count:]:
        out_lines.append(line)

    for line in out_lines:
        print(line)


if __name__ == '__main__':
    main()
