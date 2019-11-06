import os
import sys

this_module = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(this_module, "../project/"))

import sorting
from dllist import DoubleLinkedList
from random import randint

# import pytest

# number of elements in the list
max_numbers = 30

# generate a random list of numbers
def random_list(count):
    numbers = DoubleLinkedList()
    for i in range(count, 0, -1):
        numbers.shift(randint(0, 10000))
    return numbers

def debug(numbers):
    node = numbers.begin
    while node:
        print(node.value)
        node = node.next

# check if numbers are sorted
def is_sorted(numbers):
    node = numbers.begin
    while node and node.next:
        if node.value > node.next.value:
            return False
        else:
            node = node.next

    return True


def test_bubble_sort():
    numbers = random_list(max_numbers)

    sorting.bubble_sort(numbers)

    assert is_sorted(numbers)


def test_bubble_sort_opt():
    numbers = random_list(max_numbers)

    sorting.bubble_sort_opt(numbers)

    assert is_sorted(numbers)


# def test_merge_sort():
#     numbers = random_list(max_numbers)

#     sorting.merge_sort(numbers)

#     assert is_sorted(numbers)
