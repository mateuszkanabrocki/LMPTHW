#! /usr/bin/env python3
from sys import argv, exit


def main():
    """
    Examples on how to use this module:

    ./cat.py file1.txt
    ./cat.py file1.txt file2.txt
    ./cat.py file1.txt file2.txt to file3.txt
    """

    if '--help' in argv:
        print(main.__doc__)
        exit(0)

    lines = []
    try:
        with open(argv[1], 'r') as file:
            lines1 = file.read()
            lines.append(lines1)
    except:
        pass
    try:
        with open(argv[2], 'r') as file:
            lines2 = file.read()
            lines.append(lines2)
    except:
        pass

    if "to" in argv:
        index = argv.index("to")
        try:
            with open(argv[index+1], 'a+') as file:
                for i in lines:
                    file.write(i)
                file.seek(0, 0)
                lines = file.read()
                print(lines)
        except:
            pass
    else:
        for i in lines:
            print(i)


if __name__ == '__main__':
    main()