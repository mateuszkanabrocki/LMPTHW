#! /usr/bin/env python3


import argparse
from sys import exit
import re


def parse():
    help = "This module works like a sed cmdlet but it's much simpler and less functional."
    parser = argparse.ArgumentParser(description=help)
    parser.add_argument('parameters', type=str, help='command parameters')
    parser.add_argument('file', type=str, help='a file to search in')
    args = parser.parse_args()
    # print(args, '\n')
    return args


def standin():
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    return lines


def open_file(file):
    try:
        with open(file, 'r', errors='ignore') as file:
            lines = []
            for line in file.readlines():
                lines.append(line.strip('\n'))
            return lines
    except FileNotFoundError:
        print('No file found.')
        exit(1)


def parameters(args):
    parameters = args.parameters.strip("'").strip("/").split("/")
    operation = parameters[0]
    old = parameters[1]
    try:
        new = parameters[2]
    except IndexError:
        parameters.append('')
        new = parameters[2]
    # print('parameters: ', operation, old, new)
    if len(parameters) < 3:
        print('Not enough parameters.')
        exit(1)
    if args.file == '-':
        lines = standin()
        new_lines = []
        for line in lines:
            new_lines.append(re.sub(old, new, line))
            result_text = '\n'.join(new_lines)
        print(result_text)
    else:
        lines = open_file(args.file)
        text = '\n'.join(lines)
        new_lines = re.sub(old, new, text)
        with open(args.file, 'w', errors='ignore') as file:
            file.write(new_lines)


def main():
    parameters(parse())


if __name__ == '__main__':
    main()
