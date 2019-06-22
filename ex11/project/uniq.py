#! /usr/bin/env python3

from sys import stdin


def cut_standin():
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    return lines


def main():
    lines = stdin.readlines()
    uniq_lines = list(set(lines))
    for line in uniq_lines:
        print(line)


if __name__ == '__main__':
    main()


# import sys

# def print_uniq_lines(file_list):
#     all_lines = set()

#     for f in file_list:
#         all_lines |= set(f.readlines())
        
#     print("".join(all_lines))

# if len(sys.argv) > 1:
#     print_uniq_lines(open(f) for f in sys.argv[1:])
# else:
# print_uniq_lines([sys.stdin])