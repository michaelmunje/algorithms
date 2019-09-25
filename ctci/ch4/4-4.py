import unittest


class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


def check_balance(head, is_balanced):
    if head and head.value:
        h1, a = check_balance(head.left, is_balanced)
        h2, b = check_balance(head.right, is_balanced)
        is_balanced = a and b
        if abs(h1 - h2) > 1 or not is_balanced:
            return h1 + h2 + 1, False
        else:
            return h1 + h2 + 1, True

    else:
        return 0, is_balanced


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
        _, is_balanced = check_balance(head, True)
        self.assertTrue(is_balanced)
        a = [1, 3, 6, 9]
        head = list_to_bst(a)
        head.left.right = Node()
        head.left.right.value = 2
        _, is_balanced = check_balance(head, True)
        self.assertFalse(is_balanced)
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        head = list_to_bst(a)
        head.left.left = None
        head.left.right = None
        _, is_balanced = check_balance(head, True)
        self.assertFalse(is_balanced)


if __name__ == '__main__':
    unittest.main()
