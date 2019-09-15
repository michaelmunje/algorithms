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


class Heap:  # Max heap, min heap can be obtained by multipying values by -1
    def __init__(self):
        self.head = None

    def add_node(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        current_node = self.head
        stack = Stack()
        while current_node:
            stack.push(current_node)
            current_node = current_node.right
        current_node = Node(value)
        parent_node = stack.pop()
        while parent_node:
            if value > parent_node.value:
                tmp = parent_node.left
                parent_node.left = current_node.left
                current_node.left = tmp
                parent_node.right = current_node.right
                current_node.right = parent_node
                if not stack.is_empty():
                    parent_node = stack.pop()
                else:
                    parent_node = None
            else:
                break

    def tree_string(self, current_node):
        if not current_node:
            return ''
        else:
            return str(current_node.value) + '\n' \
                   + '(' + self.tree_string(current_node.left) + ')' \
                   + '(' + self.tree_string(current_node.right) + ')'

    def __repr__(self):
        return self.tree_string(self.head)


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
        heap.add_node(5)
        heap.add_node(6)
        heap.add_node(7)
        print(heap)


if __name__ == '__main__':
    unittest.main()