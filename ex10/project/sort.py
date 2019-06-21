#! /usr/bin/env python3

import argparse
from sys import exit

# 1. copy skeleton project - change names, setup.py, app.py, test file
# 2. make a script executable using: chmod +x script_name.py
# 3. think how to solve the issue - make a research if needed
# 4. note how to implement it - make a TODO list
# 5. copy a T0D0 list into the script and hash it
# 6. make any files - if needed
# 7. open terminal set virtenv and workind dir
# 8. do the things from the list, (do the test for it (or use TDD)
# 9. check the code, run the tests
# 10. do the next task

# 11. check the whole code
# 12. simplify the code and clean it
# 13. check comments
# 14. type hinting - run mypy if needed
# 15. write the documentation


# give standard input default -q
# give a file
# ls | sort
# ls | sort -r
# ls | sort -f case
# ls | sort -g num

# ls -l | ./sort.py
# ./sort.py file.txt

def parse():
    help = "This module works like a sort cmdlet but it's much simpler and less functional."
    parser = argparse.ArgumentParser(description=help)
    parser.add_argument('file', type=str, help='input file')
    parser.add_argument('-r', action='store_true', help='reverse the sorting result')
    parser.add_argument('-f', action='store_true', help='ignore letter case')
    args = parser.parse_args()
    print(args, '\n')
    return args


def cut_standin():
    text = []
    while True:
        try:
            text.append(input())
        except EOFError:
            break
    return text


def main():
    args = parse()
    if args.file == '-':
        lines = cut_standin()
        # print('lines: ', lines)
    else:
        try:
            with open(args.file, 'r', errors='ignore') as file:
                lines = file.readlines()
        except FileExistsError:
            print('File not found.')
            exit(1)
    if args.f:
        sorted_list = sorted(lines, key=lambda s: s.lower(), reverse=args.r, )  # !!for ignoring a letter case
    else:
        sorted_list = sorted(lines, reverse=args.r, )
    print()
    for line in sorted_list:
        print(line)



if __name__ == '__main__':
    main()
