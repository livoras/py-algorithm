#-*- coding: utf-8 -*-
def bubble_sort(to_sort_list):
    for compare_times in xrange(len(to_sort_list) - 1, 0, -1):
        for i in xrange(0, compare_times):
            if to_sort_list[i] > to_sort_list[i + 1]:
                tempt = to_sort_list[i]
                to_sort_list[i] = to_sort_list[i + 1]
                to_sort_list[i + 1] = tempt

to_sort_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(to_sort_list)
print to_sort_list
