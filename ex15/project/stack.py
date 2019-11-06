#!/usr/bin/env python3


class StackNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class Stack(object):

    def __init__(self):
        self._top = None

    def push(self, obj):
        """Pushes a new value to the top of the stack."""
        new_node = StackNode(obj, None)
        if self._top:
            new_node.next = self._top
        self._top = new_node

    def pop(self):
        """Pops the value that is currently on the top of the stack."""
        # if there is at least 1 element
        if self._top:
            top_value = self._top.value
            # if there are at least 2 elements
            if self._top.next:
                self._top = self._top.next
            else:
                self._top = None
            return top_value
        # if there is no element
        else:
            return None

    def top(self):
        """Returns a *reference* to the first/top item, does not remove."""
        if self._top:
            return self._top.value
        else:
            return None

    def count(self):
        """Counts the number of elements in the stack."""
        count = 0
        if self._top:
            count += 1
            node = self._top
            while node.next:
                count += 1
                node = node.next
        return count

    def dump(self, mark="----"):
        """Debugging function that dumps the contents of the stack."""
        print('')
        print(mark)
        if self._top is None:
            print('No nodes in a stack.')
            return 0
        else:
            node = self._top
            while node:
                print(node)
                node = node.next

    def _invariants(self):
        """Checking basic test cases."""
        # no nodes, top is none
        if self.count() == 0:
            assert self._top == None
        elif self.count() == 1:
            assert self._top
            assert self._top.next == None
        else:
            assert self._top
            assert self._top.next


def main():
    pass


if __name__ == '__main__':
    main()
