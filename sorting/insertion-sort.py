#-*- coding: utf-8 -*-
def insertion_sort(to_sort_list):
    for index in xrange(1, len(to_sort_list)):
        current_value = to_sort_list[index]
        pos = index
        while pos > 0 and to_sort_list[pos - 1] > current_value:
            to_sort_list[pos] = to_sort_list[pos - 1]
            pos = pos - 1
        to_sort_list[pos] = current_value    

to_sort_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(to_sort_list)
print to_sort_list
