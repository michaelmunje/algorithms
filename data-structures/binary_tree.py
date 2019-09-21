import unittest
from stack import Stack


class Node:  # Binary Node
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def binary_search(head, value):  # Returns true if value exists
    if head is None:
        return False
    elif head.value == value:
        return True
    elif head.value > value:
        return binary_search(head.left, value)
    else:
        return binary_search(head.right, value)


class Heap:  # Max heap, min heap can be obtained trivially
    def __init__(self):
        self.values = []

    def remove_max(self):
        old_max = self.values[0]
        if len(self.values) > 1:
            self.values[0] = self.values[-1]
            self.values.pop()

        i = 0

        while 2*i+1 < len(self.values):

            swap_i = 2*i+1

            if 2*i + 2 < len(self.values):
                if max(self.values[2*i+1], self.values[2*i+2]) <= self.values[i]:
                    break

                if self.values[2*i+2] > self.values[2*i+1]:
                    swap_i += 1
            else:
                if self.values[2*i+1] <= self.values[i]:
                    break

            tmp = self.values[i]
            self.values[i] = self.values[swap_i]
            self.values[swap_i] = tmp
            i = swap_i

        return old_max

    def add_node(self, value):
        self.values.append(value)
        current_i = len(self.values) - 1
        if current_i == 0:
            return

        while self.values[current_i] > self.values[current_i - 1 // 2]:
            tmp = self.values[current_i]
            self.values[current_i] = self.values[current_i - 1 // 2]
            self.values[current_i - 1 // 2] = tmp
            current_i = current_i - 1 // 2

    def tree_string(self, current_node):
        if not current_node:
            return ''
        else:
            return str(current_node.value) + '\n' \
                   + '(' + self.tree_string(current_node.left) + ')' \
                   + '(' + self.tree_string(current_node.right) + ')'

    def __repr__(self):
        return str(self.values) #self.tree_string(self.head)


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        head = Node(12)
        head.left = Node(6)
        head.right = Node(17)
        head.left.left = Node(2)
        head.left.right = Node(9)
        head.left.left.right = Node(3)
        head.right.left = Node(15)

        tree_values = [12, 6, 17, 2, 9, 3, 15]
        for i in range(30):
            if i not in tree_values:
                self.assertFalse(binary_search(head, i))
            else:
                self.assertTrue(binary_search(head, i))

    def test_case_2(self):
        head = None
        self.assertFalse(binary_search(head, 1))

    def test_case_3(self):
        heap = Heap()
        heap.add_node(25)
        heap.add_node(13)
        heap.add_node(12)
        heap.add_node(31)
        heap.remove_max()
        heap.remove_max()
        self.assertTrue(str(heap) == '[13, 12]')

    def test_case_4(self):
        heap = Heap()
        heap.add_node(31)
        heap.add_node(15)
        heap.add_node(17)
        self.assertTrue(str(heap) == '[31, 15, 17]')
        heap.add_node(2)
        heap.add_node(3)
        heap.add_node(5)
        self.assertTrue(str(heap) == '[31, 15, 17, 2, 3, 5]')
        heap.remove_max()
        self.assertTrue(str(heap) == '[17, 15, 5, 2, 3]')
        heap.remove_max()
        self.assertTrue(str(heap) == '[15, 3, 5, 2]')
        heap.remove_max()
        self.assertTrue(str(heap) == '[5, 3, 2]')


if __name__ == '__main__':
    unittest.main()