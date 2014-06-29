#-*- coding: utf-8 -*-
def binary_search(arr, item):
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
