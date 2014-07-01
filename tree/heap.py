#-*- coding: utf-8 -*-
class Heap():
    def __init__(self):
        self.arr = [None]
        self.size = 0

    def build_heap(self, arr):
        self.arr = [None] + arr
        self.size = len(arr)
        i = len(arr) / 2
        while i > 0:
            self.percolate_down(i)
            i = i - 1

    def is_empty(self):
        return self.size == 0

    def find_min():
        return self.arr[1]

    def insert(self, value):
        self.arr.append(value)
        self.size += 1 
        self.percolate_up(self.size)

    def del_min(self):
        arr = self.arr
        if self.size > 0: 
            result = arr[1]
            arr[1] = arr[self.size]
            arr.pop()
            self.size = self.size - 1
            self.percolate_down(1)
            return result
        else:
            print "Heap is empty"
            return None

    def percolate_up(self, i):
        arr = self.arr
        parent = i / 2
        if parent > 0:
            if arr[parent] > arr[i]:
                arr[parent], arr[i] = arr[i], arr[parent]
                self.percolate_up(parent)

    def percolate_down(self, i):
        # Make the smallest ones of the half of the list 
        # percolate them down to the bottom
        left = 2 * i
        right = 2 * i + 1
        smaller = i
        arr = self.arr
        length = self.size
        if left <= length and arr[left] < arr[smaller]:
            smaller = left
        if right <= length and arr[right] < arr[smaller]:
            smaller = right
        if i != smaller:
            arr[i], arr[smaller] = arr[smaller], arr[i]
            self.percolate_down(smaller)


# -------------------- Tests -------------------------------

h = Heap()
h.build_heap([9,5,6,2,3])
arr = [9,5,6,2,3]
arr.sort()
assert [h.del_min() for i in xrange(len(arr))] == arr

h = Heap()
h.build_heap([4, 1, 3, 10, 14, 8, 7])
h.insert(2)
h.insert(16)
h.insert(9)
print h.arr
assert h.del_min() == 1
assert h.del_min() == 2
assert h.del_min() == 3
assert h.del_min() == 4
assert h.del_min() == 7
assert h.del_min() == 8
assert h.del_min() == 9
assert h.del_min() == 10
assert h.del_min() == 14
assert h.del_min() == 16
