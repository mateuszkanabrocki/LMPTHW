#!/usr/bin/env python3.6

# from pathlib import Path
import os

# return the list of files in current directory
# along with their permissions


def main():
    # get names of the files
    all_files = os.listdir()
    # p = Path('.')
    # all_list = list(p.glob('*'))

    # get file permissions
    files_dict = {}
    for file in all_files:
        if os.access(file, os.R_OK):
            r = 'r'
        else:
            r = '-'
        if os.access(file, os.W_OK):
            w = 'w'
        else:
            w = '-'
        if os.access(file, os.X_OK):
            x = 'x'
        else:
            x = '-'
        files_dict[file] = ["-"+r+w+x]

    # display file names with their permissions
    for x in files_dict:
        print(files_dict[x], x)


if __name__ == '__main__':
    main()
