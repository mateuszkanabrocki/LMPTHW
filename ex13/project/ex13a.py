#!/usr/bin/env python3


# 3. think how to solve the issue - make a research if needed - make a TODO list
# 4. make any files - if needed

# 5. write code and tests (TDD, make them parallel or leave tests for the end)

# 6. check the whole code again, simplify and clean it
# 7. check comments
# 8. type hinting (run mypy if needed)
# 9. write the documentation


class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
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

    def push(self, value):
        """Appends a new value on the end of the list."""
        # create a new node
        new_node = SingleLinkedListNode(value, None)
        # if there is already a node take the last one
        # and give it's 'next' value the new node
        if self.end:
            self.end.next = new_node
        # save new node as the 'end' node
        self.end = new_node
        # if there is no node in the list save new node
        # also as the 'begin' node
        if self.begin is None:
            self.begin = new_node
        # count the new node
        self.numer_of_elements += 1

    def pop(self):
        """Removes the last item and returns it."""
        # if there is no element
        if not self.numer_of_elements:
            return None
        # last element to be poped
        poped = self.end.value
        # if there are at least 2 elements
        if self.numer_of_elements > 2:
            for i in range(self.numer_of_elements - 2):
                self.end = self.begin.next
        elif self.numer_of_elements == 2:
            self.end = self.begin
        else:
            self.end, self.begin = None, None
        self.numer_of_elements -= 1
        return poped

    def shift(self, value):
        """Add a  new element as the first one."""
        # create a new node
        new_node = SingleLinkedListNode(value, None)
        # if there is already a node take the last one
        # and give it's 'next' value the new node
        if self.begin:
            new_node.next = self.begin
        self.begin = new_node
        # if there is no node in the list save new node
        # also as the 'end' node
        if self.end is None:
            self.end = new_node
        # count the new node
        self.numer_of_elements += 1

    def unshift(self):
        """Removes the first item and returns it."""
        if not self.numer_of_elements:
            return None
        first_element = self.begin
        # save second one as begin
        if self.numer_of_elements > 1:
            self.begin = self.begin.next
        self.numer_of_elements -= 1
        return first_element.value

    def remove(self, remove):
        """Finds a matching item and removes it from the list."""
        if not self.numer_of_elements:
            return None
        current_element = self.begin
        next_element = self.begin
        for i in range(self.numer_of_elements + 1):
            if next_element.value == remove:
                current_element.next = next_element.next
                self.numer_of_elements -= 1
                if i == 0:
                    self.begin = self.begin.next
                return i
            else:
                current_element = next_element
                next_element = next_element.next  # doesn't work for the last element with no 'next' element

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

    def dump(self, mark: str):
        """Debugging function that dumps the contents of the list."""
        print(mark)
        current = self.begin
        for i in range(self.numer_of_elements):
            print(f'{current.value}')
            current = current.next
