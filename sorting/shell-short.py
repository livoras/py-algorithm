#-*- coding: utf-8 -*-
def shell_short(arr):
    sublist_count = len(arr) // 2
    while sublist_count > 0:
        for i in xrange(sublist_count):
            insert_short(arr, i, sublist_count)
        sublist_count = sublist_count // 2

def insert_short(arr, start, gap):
    for i in xrange(start, len(arr), gap):
        min_pos = i
        for j in xrange(i + gap, len(arr), gap):
            if arr[j] < arr[min_pos]:
                min_pos = j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]

to_sort_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_short(to_sort_list)
print to_sort_list
