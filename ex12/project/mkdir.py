#!/usr/bin/env python3.6

from sys import argv, exit
from os.path import exists, isfile
from os import mkdir


new_dir = argv[1:]
for file in new_dir:
    if exists(file):
        print(f"The directory '{file}' already exists.")
        exit(1)
    else:
        mkdir(file)


def main():
    pass


if __name__ == '__main__':
    main()
