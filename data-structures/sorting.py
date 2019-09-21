import unittest


class Heap:  # Min heap
    def __init__(self):
        self.values = []

    def remove_min(self):
        old_max = self.values[0]
        if len(self.values) > 1:
            self.values[0] = self.values[-1]
            self.values.pop()

        i = 0

        while 2*i+1 < len(self.values):

            swap_i = 2*i+1

            if 2*i + 2 < len(self.values):
                if min(self.values[2*i+1], self.values[2*i+2]) >= self.values[i]:
                    break

                if self.values[2*i+2] < self.values[2*i+1]:
                    swap_i += 1
            else:
                if self.values[2*i+1] >= self.values[i]:
                    break

            tmp = self.values[i]
            self.values[i] = self.values[swap_i]
            self.values[swap_i] = tmp
            i = swap_i

        return old_max

    def add_node(self, item):
        self.values.append(item)
        current_i = len(self.values) - 1
        if current_i == 0:
            return

        while current_i > 0 and self.values[current_i] < self.values[(current_i - 1) // 2]:
            tmp = self.values[current_i]
            self.values[current_i] = self.values[(current_i - 1) // 2]
            self.values[(current_i - 1) // 2] = tmp
            current_i = (current_i - 1) // 2

    def __repr__(self):
        return str(self.values)


def heap_sort(a):
    heap = Heap()
    for val in a:
        heap.add_node(val)
    for i in range(len(a)):
        a[i] = heap.remove_min()
    return a


def merge_sort_all(a):
    return merge_sort(a, 0, len(a) - 1)


def merge(a, b):
    i = 0
    j = 0
    merged_array = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged_array.append(a[i])
            i += 1
        else:
            merged_array.append(b[j])
            j += 1

    if i < len(a):
        merged_array.append(a[i])
    elif j < len(b):
        merged_array.append(b[j])

    return merged_array


def merge_sort(a, l, r):
    if r - 1 > l:
        return merge(merge_sort(a, l, (l+r) // 2), merge_sort(a, (l+r) // 2 + 1, r))
    elif l == r:
        return [a[l]]
    else:
        return [a[l], a[r]] if a[l] < a[r] else [a[r], a[l]]


def bubble_sort(a):
    sorts_happened = True
    while sorts_happened:
        sorts_happened = False
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                sorts_happened = True
    return a


def insertion_sort(a):
    for i in range(1, len(a)):
        if a[i-1] > a[i]:
            tmp = a[i]
            shift = 0
            for j in range(0, i):
                if tmp <= a[j]:
                    shift = j
                    break
            for j in range(0, i - shift):
                a[i - j] = a[i - j - 1]
            a[shift] = tmp

    return a


def selection_sort(a):
    if not a:
        return a

    for i in range(len(a)):
        minimum = a[i]
        minimum_index = i
        for j in range(i, len(a)):
            if a[j] < minimum:
                minimum = a[j]
                minimum_index = j
        a[i], a[minimum_index] = a[minimum_index], a[i]
    return a


def quick_sort(a):
    return quick_sort_rec(a, 0, len(a) - 1)


def quick_sort_rec(a, l, r):
    if l < r:
        pivot = a[r]
        i = l
        for j in range(l, r):
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[r] = a[r], a[i]

        quick_sort_rec(a, l, i - 1)
        quick_sort_rec(a, i + 1, r)


class TestSolution(unittest.TestCase):

    def test_case1(self):
        a = [5, 2, 1, 4, 2, 1]
        self.assertEqual(heap_sort(a), [1, 1, 2, 2, 4, 5])
        a = [5, 2, 1, 4, 2, 1, 10]
        self.assertEqual(heap_sort(a), [1, 1, 2, 2, 4, 5, 10])

    def test_case2(self):
        a = [5, 2, 1, 4, 2, 1]
        self.assertEqual(bubble_sort(a), [1, 1, 2, 2, 4, 5])
        a = [5, 2, 1, 4, 2, 1, 10]
        self.assertEqual(bubble_sort(a), [1, 1, 2, 2, 4, 5, 10])

    def test_case3(self):
        a = [1, 2, 3]
        self.assertEqual(insertion_sort(a), [1, 2, 3])
        a = [3, 2, 1]
        self.assertEqual(insertion_sort(a), [1, 2, 3])
        a = [5, 2, 1, 4, 2, 1]
        self.assertEqual(insertion_sort(a), [1, 1, 2, 2, 4, 5])
        a = [5, 2, 1, 4, 2, 1, 10]
        self.assertEqual(insertion_sort(a), [1, 1, 2, 2, 4, 5, 10])

    def test_case4(self):
        a = [1, 2, 3]
        self.assertEqual(selection_sort(a), [1, 2, 3])
        a = [3, 2, 1]
        self.assertEqual(selection_sort(a), [1, 2, 3])
        a = [5, 2, 1, 4, 2, 1]
        self.assertEqual(selection_sort(a), [1, 1, 2, 2, 4, 5])
        a = [5, 2, 1, 4, 2, 1, 10]
        self.assertEqual(selection_sort(a), [1, 1, 2, 2, 4, 5, 10])

    def test_case5(self):
        a = [1, 2, 3]
        quick_sort(a)
        self.assertEqual(a, [1, 2, 3])
        a = [3, 2, 1]
        quick_sort(a)
        self.assertEqual(a, [1, 2, 3])
        a = [5, 2, 1, 4, 2, 1]
        quick_sort(a)
        self.assertEqual(a, [1, 1, 2, 2, 4, 5])
        a = [5, 2, 1, 4, 2, 1, 10]
        quick_sort(a)
        self.assertEqual(a, [1, 1, 2, 2, 4, 5, 10])


if __name__ == '__main__':
    unittest.main()