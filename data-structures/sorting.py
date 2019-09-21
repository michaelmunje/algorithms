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


class TestSolution(unittest.TestCase):

    def test_case1(self):
        a = [5, 2, 1, 4, 2, 1]
        self.assertEqual(heap_sort(a), [1, 1, 2, 2, 4, 5])


if __name__ == '__main__':
    unittest.main()