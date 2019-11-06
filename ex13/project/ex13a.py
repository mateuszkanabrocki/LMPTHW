#!/usr/bin/env python3

from typing import Optional


class SingleLinkedListNode(object):

    def __init__(self, value, nxt: 'SingleLinkedListNode'):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"


class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None
        self.numer_of_elements = 0

    def push(self, value) -> None:
        """Appends a new value on the end of the list."""
        new_node = SingleLinkedListNode(value, None)
        # if any node
        if self.end and self.begin:
            self.end.next = new_node
        else:
            self.begin, self.end = new_node, new_node
        self.end = new_node
        # count the new node
        self.numer_of_elements += 1

    def pop(self) -> Optional[SingleLinkedListNode]:
        """Removes the last item and returns it."""
        if not self.numer_of_elements:
            return None
        last_element = self.end.value
        # changes after poping:
        if self.numer_of_elements > 2:
            for i in range(self.numer_of_elements - 2):
                self.end = self.begin.next
        elif self.numer_of_elements == 2:
            self.end = self.begin
        else:
            self.end, self.begin = None, None
        self.numer_of_elements -= 1
        return last_element

    def shift(self, value) -> None:
        """Add a new element at the last position."""
        self.push(value)

    def unshift(self) -> Optional[SingleLinkedListNode]:
        """Removes the first item and returns it."""
        first_element = self.begin
        # save second one as begin
        if self.numer_of_elements > 1:
            self.begin = self.begin.next
        elif self.numer_of_elements == 1:
            self.begin, self.end = None, None
        else:
            return None
        self.numer_of_elements -= 1
        return first_element.value

    def remove(self, remove) -> Optional[int]:
        """Finds a matching item and removes it from the list."""
        if self.numer_of_elements:
            current_element = self.begin
            next_element = self.begin
            for i in range(self.numer_of_elements + 1):
                if next_element.value == remove:
                    current_element.next = next_element.next
                    self.numer_of_elements -= 1
                    # it was a first element
                    if i == 0:
                        self.begin = self.begin.next
                    return i
                else:
                    current_element = next_element
                    try:
                        next_element = next_element.next
                    except:
                        print('No element found.')
        else:
            return None
      
    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end.value

    def count(self):
        """Counts the number of elements in the list."""
        # return number of nodes
        return self.numer_of_elements

    def get(self, index):
        """Get the value at index."""
        if self.numer_of_elements > index:
            index_value = self.begin
            for i in range(index):
                index_value = index_value.next
            return index_value.value
        else:
            return None

    def dump(self, mark: str) -> None:
        """Debugging function that dumps the contents of the list."""
        print(mark)
        current = self.begin
        for i in range(self.numer_of_elements):
            print(f'{current.value}')
            current = current.next
