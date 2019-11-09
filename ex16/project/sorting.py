#!/usr/bin/env python3

from dllist import DoubleLinkedList

def length(numbers):
    """Return list length."""
    try:
        node = numbers.begin
    except AttributeError:
        return None
    
    count = 0
    while node:
        count += 1
        node = node.next

    return count

def bubble_sort(numbers):
    """Sorts a list of numbers using bubble sort."""
    while True:
        # start off assuming it's sorted
        is_sorted = True
        # comparing 2 at a time, skipping ahead
        node = numbers.begin.next
        while node:
            # loop through comparing node to the next
            if node.prev.value > node.value:
                # if the next is greater, then we need to swap
                node.prev.value, node.value = node.value, node.prev.value
                # oops, looks like we have to scan again
                is_sorted = False
            node = node.next

        # this is reset at the top but if we never swapped then it's sorted
        if is_sorted: break


def bubble_sort_opt(numbers):
    """Sorts a list of numbers using bubble sort."""
    while True:
        # start off assuming it's sorted
        is_sorted = True
        node = numbers.begin.next
        count = 1 # count checks to know the swapped_position
        swapped_position = length(numbers)-1 # start off position
        while node:
            # neglect last check - as it's already sorted
            # neglect positions after swap at the last passing through the list
            if count >= (swapped_position - 1):
                break
            # loop through comparing node value to the next one
            if node.prev.value > node.value:
                # swap
                node.prev.value, node.value = node.value, node.prev.value
                # oops, looks like we have to scan again
                is_sorted = False
                swapped_position = count # memorise the last swap position
            node = node.next
            count =+ 1 

        # if we do not swap then it's sorted
        # this is reset at the top
        if is_sorted: break


def merge_sort(numbers):
    """Sorts a list of numbers using merge sort."""
    sorted = merge_sort_core(numbers)
    # empty numbers
    node = numbers.begin
    while node:
        numbers.detach_node(node)
        node = node.next
    # overwrite
    node_sort = sorted.begin
    while node_sort:
        numbers.push(node_sort)
        node_sort = node_sort.next

def merge_sort_core(numbers):
    """Merge sort algorithm."""
    if length(numbers) <= 1:
        return numbers

    left = DoubleLinkedList()
    right = DoubleLinkedList()
    for i in range(length(numbers)):
        x = numbers.begin
        for j in range(i):
            x = x.next
        # split the list into two
        if i < (length(numbers)/2):
            left.push(x.value)
        else:
            right.push(x.value)
    # split result lists into another smaller lists recursively
    left = merge_sort_core(left)
    right = merge_sort_core(right)
    
    # return merged lists with sorted elements
    return merge(left, right)

def merge(left, right):
    """Merge list while sorting their elements"""
    result = DoubleLinkedList()
    # while both lists are not empty
    while length(left) and length(right):
        left_node = left.begin
        right_node = right.begin

        if left_node.value <= right_node.value:
            result.push(left.unshift())
        else:
            result.push(right.unshift())
    # while left list is not empty
    while left.begin: 
        result.push(left.unshift())
    # while right list is not empty
    while right.begin:
        result.push(right.unshift())

    return result



def main():
    pass


if __name__ == '__main__':
    main()
