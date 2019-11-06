#!/usr/bin/env python3


def count_list(numbers):
    node = numbers.begin
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
        # comparing 2 at a time, skipping ahead
        node = numbers.begin.next
        count = 1 # count checks to know the swapped_position
        swapped_position = count_list(numbers)-1 # start off value
        # do x
        while node:
            # loop through comparing node to the next
            if count >= (swapped_position - 1):
                break
            if node.prev.value > node.value:
                # if the next is greater, then we need to swap
                node.prev.value, node.value = node.value, node.prev.value
                # oops, looks like we have to scan again
                is_sorted = False
                swapped_position = count # memorise the last swap position
            node = node.next
            count =+ 1 

        # this is reset at the top but if we never swapped then it's sorted
        if is_sorted: break




# def merge_sort(m):
#     if length of m ≤ 1 then
#         return m

#     var left := empty list
#     var right := empty list
#     for each x with index i in m do
#         if i < (length of m)/2 then
#             add x to left
#         else
#             add x to right

#     left := merge_sort(left)
#     right := merge_sort(right)

#     return merge(left, right)

# function merge(left, right)
#     var result := empty list

#     while left is not empty and right is not empty do
#         if first(left) ≤ first(right) then
#             append first(left) to result
#             left := rest(left)
#         else
#             append first(right) to result
#             right := rest(right)

#     while left is not empty do
#         append first(left) to result
#         left := rest(left)
#     while right is not empty do
#         append first(right) to result
#         right := rest(right)
#     return result




def main():
    pass


if __name__ == '__main__':
    main()
