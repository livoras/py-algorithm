#-*- coding: utf-8 -*-
def selection_sort(to_sort_list):
    for pos in xrange(0, len(to_sort_list)):
        min_pos = pos
        for to_compare_pos in xrange(pos + 1, len(to_sort_list)):
            if to_sort_list[to_compare_pos] < to_sort_list[min_pos]:
                min_pos = to_compare_pos
        if min_pos != pos:        
            tempt = to_sort_list[min_pos]
            to_sort_list[min_pos] = to_sort_list[pos]
            to_sort_list[pos] = tempt

to_sort_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(to_sort_list)
print to_sort_list
