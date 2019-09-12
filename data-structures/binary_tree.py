import unittest


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


if __name__ == '__main__':
    unittest.main()