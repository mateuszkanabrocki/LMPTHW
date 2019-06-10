#! /usr/bin/env python3


#Cheat sheet

# parser = argparse.ArgumentParser(description='Process some integers.')  # make a parser object

# parser.add_argument('integers', metavar='N', type=int, nargs='+', # add information about program arguments
#                      help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                      const=sum, default=max,
#                      help='sum the integers (default: find the max)')
# parser.add_argument('--foo', help='foo help') # If -h or --help is supplied at the command line, the ArgumentParser help will be printed
# parser.add_argument('--foo') # default store action
# parser.add_argument('--foo', action='store_const', const=42) # store const value
# parser.add_argument('--baz', action='store_false') # store bool falue
# parser.add_argument('--foo', nargs=2) # set the number of arguments
# parser.add_argument('--foo', nargs='*') # all arguments given
# parser.add_argument('--foo', action='append') # store multiple foo values into single list of values (>>> parser.parse_args('--foo 1 --foo 2'.split())
# Namespace(foo=['1', '2']))
# parser.add_argument('--version', action='version', version='%(prog)s 2.0')
                     
# parser.parse_args(['--sum', '7', '-1', '42']) # parse arguments to the object

# # (In a script, parse_args() will typically be called with no arguments, and the ArgumentParser will automatically determine the command-line # arguments from sys.argv.)

# LMPTHW
#import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('integers', metavar='N', type=int, nargs='+')
# parser.add_argument('-f', '--foo', help='foo help')
# parser.add_argument('-b', '--bar', help='bar help')
# parser.add_argument('-z', '--baz', help='baz help')
# parser.add_argument('-t', '--turn-on', action='store_true')
# parser.add_argument('-x', '--exclude', action='store_false')
# parser.add_argument('-s', '--start', action='store_true')
# args = parser.parse_args()


import argparse


def main():
    parser = argparse.ArgumentParser(description='This is an argparse module test.')  # getting help with --help and -h
    parser.add_argument('--shout', action='store_const', const='Hi!', help='The shout mode.')  # 3 flags (they don't take an extra argument but simply putting them on the command line turns something on)
    parser.add_argument('--silent', action='store_const', const='hi', help='The silent mode.')
    parser.add_argument('--add', '--a', nargs='*', help='Add numbers.')  # 3 arguments that are options - take an argument and set
    parser.add_argument('--subtract', '--s', nargs='*', help='Subtract numbers.')
    parser.add_argument('--multiply', '--m', nargs='*', help='Multiply numbers.')
    parser.add_argument('--files', '--f', nargs=2, help='File with numbers to operate and the write file.') 
    args = parser.parse_args()

    print('>>>', args)

    # if '--add' in args:
    #     print(args.accumulate(1, 3))

    print(args)

if __name__ == '__main__':
    main()