#! /usr/bin/env python3


def cut_standin():
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    return lines


def main():
    lines = cut_standin()
    uniq_lines = list(set(lines))
    for line in uniq_lines:
        print(line)


if __name__ == '__main__':
    main()
