import unittest
import sys


class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


def is_bst(root):
    if not root:
        return True

    q = []
    q.insert(0, (root, -sys.maxsize - 1, sys.maxsize))

    while q:
        node, lower, upper = q.pop()

        if not lower < node.value < upper:
            return False

        if node.left:
            if node.left.value:
                q.insert(0, (node.left, lower, node.value))

        if node.right:
            if node.right.value:
                q.insert(0, (node.right, node.value, upper))

    return True


def list_to_bst(a):
    head = Node()
    list_to_bst_rec(a, 0, len(a), head)
    return head


def list_to_bst_rec(a, l, r, node):
    if l < r:
        mid = (l + r) // 2
        node.value = a[mid]
        node.left = Node()
        list_to_bst_rec(a, l, mid, node.left)
        node.right = Node()
        list_to_bst_rec(a, mid + 1, r, node.right)


class TestSolution(unittest.TestCase):
    def test_stacks(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        head = list_to_bst(a)
        self.assertTrue(is_bst(head))
        a = [1, 2, 3, 4, 9, 6, 7, 8, 9]
        head = list_to_bst(a)
        self.assertFalse(is_bst(head))
        a = [1, 2, 3, 9, 5, 6, 7, 8, 9]
        head = list_to_bst(a)
        self.assertFalse(is_bst(head))
        a = [1, 2, 3, 9, 5, 10, 7, 8, 9]
        head = list_to_bst(a)
        self.assertFalse(is_bst(head))


if __name__ == '__main__':
    unittest.main()
