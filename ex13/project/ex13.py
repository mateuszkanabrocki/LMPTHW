#!/usr/bin/env python3


# 3. think how to solve the issue - make a research if needed - make a TODO list
# 4. make any files - if needed

# 5. write code and tests (TDD, make them parallel or leave tests for the end)

# 6. check the whole code again, simplify and clean it
# 7. check comments
# 8. type hinting (run mypy if needed)
# 9. write the documentation


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
