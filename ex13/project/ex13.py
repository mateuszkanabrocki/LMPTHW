#!/usr/bin/env python3


class SingleLinkedList(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.value and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


def main():
    pass


if __name__ == '__main__':
    main()
