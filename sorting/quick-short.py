#-*- coding: utf-8 -*-
import random

def quick_sort(arr):
    q_sort(arr, 0, len(arr) - 1)

def q_sort(arr, start, end):
    if start >= end: return
    split_point = partition(arr, start, end)
    q_sort(arr, start, split_point - 1)
    q_sort(arr, split_point + 1, end)

def partition(arr, start, end):
    privot, privot_index = get_three_median(arr, start, end)
    left = start
    right = end
    while True:
        while arr[left] <= privot and left < end:
            left = left + 1
        while arr[right] >= privot and right > start:
            right = right - 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            if privot_index > left:
                arr[privot_index], arr[left] = arr[left], arr[privot_index]
                return left
            elif privot_index < right:    
                arr[privot_index], arr[right] = arr[right], arr[privot_index]
                return right
            else:
                return privot_index

def get_three_median(arr, start, end):
    middle = (start + end) // 2
    if arr[start] >= arr[end]:
        bigger = start
        smaller = end
    else:    
        bigger = end
        smaller = start
    if arr[bigger] <= arr[middle]:
        return arr[bigger], bigger
    else:
        if arr[smaller] >= arr[middle]:
            return arr[smaller], smaller
        else:
            return arr[middle], middle

to_sort_list = [random.randint(0, 100) for i in range(1, 101)]
quick_sort(to_sort_list)
print to_sort_list

to_sort_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(to_sort_list)
print to_sort_list
