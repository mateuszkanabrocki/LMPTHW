#! /usr/bin/env python3

import argparse
import os


def parse():
    main_help = """
    Examples on how to use this module:

    ./find.py [file_path] -name "*.txt"
    ./find.py [file_path] -name "*.txt" -print
    ./find.py [file_path] -type d -print
    ./find.py ./.. -name "*1.txt" -exec cat {} \;
    """

    parser = argparse.ArgumentParser(description=main_help)  
    parser.add_argument('given_path', help='give a search path')
    parser.add_argument('-name', help='search for files by a file name')
    parser.add_argument('-type', help='search for files by a file type')
    parser.add_argument('-print', action='count', help='print the found files')
    parser.add_argument('-exec', nargs='+', help='execute cmdlet on the found files')
    args = parser.parse_args()
    # print('\nargs: ', args)
    return args


def find_files(args):
    file_list = os.listdir(args.given_path)
    # print('\nfile_list: ', file_list)

    if args.name:
        strip_name = args.name.strip('"')
        strip_name = args.name.strip("'")
        strip_name = args.name.strip('*')
        found_files = []
        for file in file_list:
            if strip_name in file:
                found_files.append(file)
                # print('\n')
                # print("found_files: ", found_files)
    elif args.type:
        if args.type == 'd':  # d stands for directories
            found_files = []
            for file in file_list:
                if '.' not in file:
                    found_files.append(file)
        elif args.type == 'f':  # f stands for files not directories
            found_files = []
            for file in file_list:
                if '.' in file:
                    found_files.append(file)
                    # print('\n')
                    # print('found files: ', found_files)
    return found_files


def do(found_files, args):
    if args.print and found_files:
        print('\n\n')
        for found in found_files:
            print(found)
    elif args.exec and found_files:
        print('\n\n')
        for found in found_files:
            exec_string = ' '.join(args.exec)
            exec_strip = exec_string.strip(';')
            exec_strip = exec_strip.strip('\\')
            file_path = args.given_path + '/' + found
            command = exec_strip.format(file_path)
            os.system(command)
            print('\n\n')


def main():
    args = parse()
    found_files = find_files(args)
    do(found_files, args)


if __name__ == '__main__':
    main()


# LMPTHW

# from pathlib import Path
# import sys
# import argparse

# def name_find(start, args):
#     for f in start.rglob(args.name):
#         print(f)

# def type_find(start, args):
#     if args.type not in ['d','f']:
#         print(f"Unknown type: {args.type}")
#         sys.exit(1)

#     for f in start.rglob(args.name or "*"):
#         if args.type == "d" and f.is_dir():
#             print(f)
#         elif args.type == "f" and f.is_file():
#             print(f)


# def find_files(args):
#     start_path = Path(args.start[0])
    
#     if args.name and not args.type:
#         name_find(start_path, args)
#     elif args.type:
#         type_find(start_path, args)
#     else:
#         print("You need either --name or --type")
#         sys.exit(1)

# def parse_args():
#     parser = argparse.ArgumentParser()

#     parser.add_argument('start', type=str, nargs=1) 
#     parser.add_argument('--name', type=str)
#     parser.add_argument('--type' , type=str)

#     return parser.parse_args()

# find_files(parse_args())
