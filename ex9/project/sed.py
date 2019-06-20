#! /usr/bin/env python3


import argparse
from sys import exit
import re

def parse():
    help = "This module works like a sed cmdlet but it's much simpler and less functional."
    parser = argparse.ArgumentParser(description=help)
    parser.add_argument('parameters', type=str, help='command parameters')
    parser.add_argument('file', type=str, help='a file to search in')
    # parser.add_argument('-d', type=str, help='a character to separate columns of data', default='   ')
    # parser.add_argument('-f', help='number of column to be displayed')
    args = parser.parse_args()
    print(args, '\n')
    return args



# sed 's/[A-Z]/X/g'
# sed '/^daemon/dodo' (change all first 'deamon' words in each line)



def parameters(args):
    parameters = args.parameters.strip("'").strip("/").split("/")
    operation = parameters[0]
    old = parameters[1]
    new = parameters[2]
    print('parameters: ', operation, old, new)
    if len(parameters) < 3:
        print('Not enough parameters.')
        exit(1)

    try:
        with open(args.file, 'r', errors='ignore') as file:
            lines = []
            for line in file.readlines():
                lines.append(line.strip('\n'))
            print('lines: ', lines)
    except FileNotFoundError:
        print('No such file.')
        exit(1)
    text = '\n'.join(lines)
    new_lines = re.sub(old, new, text)
    # new_lines = ''
    # for line in lines:
    #     words = []
    #     words = line.split(' ')
    #     new_words = []
    #     for word in words:
    #         if re.findall(old, word):
    #             new_words.append(new)
    #         else:
    #             new_words.append(word)
    #     new_lines += ' '.join(new_words) + '\n'

    # new_lines = []
    # if len(parameters) >= 4 and parameters[3] == 'g':
    #     print('here!')
    #     for line in lines:
    #         new_lines.append(line.replace(old, new))
    #     print('new_lines: ', new_lines)
    # else:
    #     for line in lines:
    #         new_lines.append(line.replace(old, new, 1))
    #     print('new_lines: ', new_lines)

    with open(args.file, 'w', errors='ignore') as file:
        file.write(new_lines)

def main():
    parameters(parse())


if __name__ == '__main__':
    main()
