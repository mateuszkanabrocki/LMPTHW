#!/usr/bin/env python3.6

from sys import argv
import sys

# how to use:
# history|tail -3|./yes.py
# cat file.txt | ./yes.py


# if stdin given
if not sys.stdin.isatty():
    in_list = sys.stdin.readlines()
    string = '\n'.join(in_list)
    print(string)
else:
    string = argv[1]
while True:
    print(string)
















def main():
    pass


if __name__ == '__main__':
    main()
