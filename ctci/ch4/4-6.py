import unittest
import sys


class Node:
    def __init__(self):
        self.value = None
        self.parent = None
        self.left = None
        self.right = None


def find_successor(node):   # Tests not included due to lack of parent implementation.
    if not node:
        return None

    if node.right:
        return get_leftmost(node.right)
    else:
        q = node
        p = q.parent
        while p and p.left != q:
            q = p
            p = p.parent
        return parent


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


if __name__ == '__main__':
    unittest.main()
