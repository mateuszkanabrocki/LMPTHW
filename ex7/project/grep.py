#! /usr/bin/env python3

import argparse
from sys import exit
from pathlib import Path
import re


def parse():
    help = "This module works like a grep cmdlet but it's much simpler and less functional."
    parser = argparse.ArgumentParser(description=help)
    parser.add_argument('-i', action='store_true', help='ignore words case while searching')
    parser.add_argument('search', help='a literal or a regex to search for')
    parser.add_argument('file', type=str, help='a file name to search in')
    args = parser.parse_args()
    print(args, '\n')
    return args


def find_files(args):
    files_found = sorted(Path('.').glob(args.file))
    if not files_found:
        print("No file found.")
        exit(1)
    return files_found

    # # for the absolute file path:
    # files_found_abs = []
    # for file_found in files_found:
    #     files_found_abs.append(file_found.resolve())
    # return files_found_abs


def main():
    args = parse()
    if args.file == "-":
        standin = input("Type a text here:\n>")
        standin_lines = standin.split('\n')
        search(args, standin_lines)
    else:
        files_found_abs = find_files(args)
        for found in files_found_abs:
            try:
                with open(str(found), 'r') as file:
                    print('Found a file:', found)
                    lines = file.readlines()
                    search(args, lines)
            except FileNotFoundError:
                print("No such text file.")
                exit(1)


def search(args, lines):
    search = args.search.strip('"')
    print("Lines found:")
    for line in lines:
        if re.findall(args.search, line):
            print(line)


if __name__ == '__main__':
    main()
