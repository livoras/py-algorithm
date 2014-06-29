#-*- coding: utf-8 -*-
def binary_search(arr, item):
'''
Using two cursor `left` and `right` and continously ajust them
by comparing the middle position between them util left is less 
than right or util the value of middle position is the same as
the value to be looked for.
'''
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) / 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:    
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [17, 20, 26, 31, 44, 54, 55, 77, 93]
assert binary_search(arr, 31) == 3
assert binary_search(arr, 17) == 0
