#! /usr/bin/env python3
from sys import exit
import argparse


def main():

    main_help = """
    Examples on how to use this module:

    ./cat.py file1.txt
    ./cat.py file1.txt --to file2.txt
    ./cat.py file1.txt --output file2.txt  # same as previous one
    ./cat.py file1.txt file2.txt --to file3.txt
    """

    parser = argparse.ArgumentParser(description=main_help)  
    parser.add_argument('input', nargs='*', help='Add input file names.')
    parser.add_argument('--output', '--to', help='Add output file name.')
    args = parser.parse_args()
    # print(args)

    if args.input:
        lines = []
        for file in args.input:
            try:
                with open(file, 'r') as file:
                    # lines.append(file.read())
                    lines.append(file.read())
            except:
                continue

    if args.output:
        print('\nOutput file:\n')
        try:
            with open(args.output, 'a+') as file:
                for line in lines:
                    file.write(line)
                file.seek(0, 0)
                print(file.read())
        except:
            pass
    else:
        if args.input:
            print('\nInput:\n')
            for file in args.input:
                try:
                    with open(file, 'r') as file:
                        print(file.read(),'\n')
                except:
                    continue


if __name__ == '__main__':
    main()