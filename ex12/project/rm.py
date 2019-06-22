#!/usr/bin/env python3.6

from sys import argv
import os
import os.path
# rm file1.txt file2.txt


def main():
    files = argv[1:]
    for file in files:
        # check if path exists (dir or file)
        if os.path.exists(file):
            # check file write permissions
            if not os.access(file, os.W_OK):
                print(f" File '{file}' do not have th write permissions.\n",
                    "Are you sure you want to remove it?\n> ")
                delete = input()
                if 'yes' in delete:
                    os.remove(file)
                    print(f"File '{file}' was removed.")
                    exit(0)
                else:
                    print(f"File '{file}' wasn't removed.")
                    exit(0)
            try:
                os.remove(file)
                print(f"File '{file}' was removed.")
            except IsADirectoryError:
                print("Can't remove directories.")
                exit(1)
        else:
            print(f"File '{file}' not found.")
            exit(1)


if __name__ == '__main__':
    main()
