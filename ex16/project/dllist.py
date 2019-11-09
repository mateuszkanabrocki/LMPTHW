#!/usr/bin/env python3

class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"


class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        # end shouldn't be given here
        self.end = None 
    
    def detach_node(self, node):
        """You'll need to use this operation sometimes, but mostly 
        inside remove().  It should take a node, and detach it from
        the list, whether the node is at the front, end, or in the middle."""
        node.prev = None
        node.next = None

    def count(self):
        """Counts the number of elements in the list."""
        node = self.begin
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def _invariants(self):
        """Checking basic test cases."""
        number = self.count()
        if number is 0:
            assert self.begin is None
            assert self.end is None
        elif number is 1:
            assert self.begin is self.end
            assert self.begin.prev is None
            assert self.end.next is None
        else:
            assert self.begin.prev is None
            assert self.end.next is None

    def unshift(self):
        """Removes the first item (from begin) and returns its value."""
        # if there is no elements
        if self.begin is None:
            return None
        # if there is one element
        elif self.begin is self.end:
            node = self.begin
            self.begin = None
            self.end = None
        # if there is more elements
        else:
            node = self.begin
            self.begin = self.begin.next
            self.begin.prev = None
        self.detach_node(node)
        return node.value

    def push(self, value):
        """Appends a new value on the end of the list."""
        # self._invariants()
        new_node = DoubleLinkedListNode(value, None, self.end)
        # if there is no element
        if self.begin is None:
            # assign the new element to the begin and the end
            self.begin = new_node
            self.end = new_node
        # if there are elements
        else:
            self.end.next = new_node
            # new_node.prev = self.end (already done)
            self.end = new_node

    def pop(self):
        """Removes the last item and returns it."""
        end = self.end
        # if there is no elements
        if self.begin is None:
            return None
        # if there is one element
        elif self.begin is self.end:
            self.begin = None
            self.end = None
            self.detach_node(end)
            return end.value
        # if there are 2 or more elements
        else:
            self.end.prev.next = None
            self.end = self.end.prev
            self.detach_node(end)
            return end.value
        
    def shift(self, value):
        """Actually just another name for push."""
        self.push(value)

    def remove(self, value):
        """Finds a matching item and removes it from the list."""
        node = self.begin
        count = 0
        while node:
            if node.value == value:
                # if there is one node
                if self.begin is self.end:
                    self.begin = None
                    self.end = None
                # if there is more nodes
                else:
                    # if it's the first one
                    if node == self.begin:
                        self.begin = node.next
                        self.begin.prev = None
                    # if it's the last one
                    elif node == self.end:
                        self.end = node.prev
                        self.end.next = None
                    # if it's the middle one
                    else:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                break
            else:
                node = node.next
                count += 1
        self.detach_node(node)
        return count

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end.value

    def get(self, index):
        """Get the value at index."""
        if self.count() > index:
            index_value = self.begin
            for i in range(index):
                index_value = index_value.next
            return index_value.value
        else:
            return None

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        node = self.begin
        count = 0
        print('')
        while node:
            print(count, '>>>', node.value)
            count += 1
            if node is not self.end:
                node = node.next
            else:
                break
        print('self.begin >>', self.begin)
        print('self.end >>', self.end)


def main():
    pass

if __name__ == '__main__':
    main()
