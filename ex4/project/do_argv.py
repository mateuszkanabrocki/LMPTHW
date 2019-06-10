#! /usr/bin/env python3.6

from sys import argv, exit

# check if there are arguments given for the optional argument
def check_arg(argv, index):
    # print('index: ', index)
    numbers = []
    for argument in argv[index+1:]:
        # print('argv[index+1:]: ', argv[index+1:])
        # print('argument: ', argument)
        try:
            int(argument)
            numbers.append(argument)
            # print('number arguments: ', numbers)
        except ValueError:
            pass
    # print('returning')
    return numbers
# check arguments of the math operation


def check_help(argv):
    # check if there is --help
    if len(argv) >= 2:
        if argv[1] == '--help':
            print('The help description.')
            exit(0)
        else:
            pass
    else:
        pass
    # return help string


def check_modes(argv):
    # check if there is --shout_mode or --gently_mode
    for word in argv:
        if word == '--shout_mode':
            print('\nHelloo!!!\n')
        elif word == '--silent_mode':
            print('\nhi...\n')
        else:
            pass
    # print the relevant string


def check_files(argv):
    files = []
    for argument in argv:
        if '.txt' in argument:
            files.append(argument)
    return files


def add(numbers_given, files_names):
    sum = 0
    for number in numbers_given:
        sum += int(number)
        print('>>>>', sum)
    if len(files_names) >= 2:
        try:
            with open(files_names[0], 'r') as file_first:
                numbers = file_first.readlines()
                print('lines1: ', numbers)
                numbers_stripped = []
                for line in numbers:
                    numbers_stripped.append(line.strip('\n'))
                print('numbers FILE: ', numbers_stripped)
                for i in numbers_stripped:
                    try:
                        sum += int(i)
                        print("SUM: ", sum)
                    except TypeError:
                        continue
        except FileNotFoundError:
            pass
        try:
            with open(files_names[1], 'w') as file_second:
                numbers = file_second.write(str(sum))
        except FileNotFoundError:
            pass
    return sum


def subtract(numbers, files_names):
    diff = int(numbers[0])
    # print('diff: ', diff)
    for number in numbers[1:]:
        # print('number: ', number)
        diff -= int(number)
        # print('diff: ', diff)
    if len(files_names) >= 2:
        try:
            with open(files_names[0], 'r') as file_first:
                numbers = file_first.readlines()
                print('lines1: ', numbers)
                numbers_stripped = []
                for line in numbers:
                    numbers_stripped.append(line.strip('\n'))
                print('numbers FILE: ', numbers_stripped)
                for i in numbers_stripped:
                    try:
                        diff -= int(i)
                        print("DIFF: ", diff)
                    except TypeError:
                        continue
        except FileNotFoundError:
            pass
        try:
            with open(files_names[1], 'w') as file_second:
                numbers = file_second.write(str(diff))
        except FileNotFoundError:
            pass
    return diff


def multiply(numbers, files_names):
    mult = int(numbers[0])
    for number in numbers[1:]:
        mult *= int(number)
    if len(files_names) >= 2:
        try:
            with open(files_names[0], 'r') as file_first:
                numbers = file_first.readlines()
                print('lines1: ', numbers)
                numbers_stripped = []
                for line in numbers:
                    numbers_stripped.append(line.strip('\n'))
                print('numbers FILE: ', numbers_stripped)
                for i in numbers_stripped:
                    try:
                        mult *= int(i)
                        print("MULT: ", mult)
                    except TypeError:
                        continue
        except FileNotFoundError:
            pass
        try:
            with open(files_names[1], 'w') as file_second:
                numbers = file_second.write(str(mult))
        except FileNotFoundError:
            pass
    return mult


def math_operation(argv):
    for argument in argv:
        print('argument: ', argument)
        if '--add' in argv:
            # print('operation: add')
            result = add(check_arg(argv, argv.index('--add')),
                         check_files(argv))
            print(f'\nSum: {result}')
            break
        elif '--subtract' in argv:
            # print('operation: subtract')
            result = subtract(check_arg(argv, argv.index('--subtract')),
                              check_files(argv))
            print(f'\nSum: {result}')
            break
        elif '--multiply' in argv:
            # print('operation: multiply')
            result = multiply(check_arg(argv, argv.index('--multiply')),
                              check_files(argv))
            print(f'\nSum: {result}')
            break
        else:
            pass


def main():
    check_help(argv)
    check_modes(argv)
    math_operation(argv)


if __name__ == '__main__':
    main()