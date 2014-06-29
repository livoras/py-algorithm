#-*- coding: utf-8 -*-
import random

def shell_short(arr):
    sublist_count = len(arr) // 2
    while sublist_count > 0:
        for i in xrange(sublist_count):
            insert_sort(arr, i, sublist_count)
        sublist_count = sublist_count // 2

def insert_sort(arr, start, gap):
    for i in xrange(start + gap, len(arr), gap):
        val = arr[i]
        pos = i
        while pos > start and arr[pos - gap] > val:
            arr[pos] = arr[pos - gap]
            pos = pos - gap
        arr[pos] = val

to_sort_list = [random.randint(0, 100) for i in range(1, 101)]
shell_short(to_sort_list)
print to_sort_list
