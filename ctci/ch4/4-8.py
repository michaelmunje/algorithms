import unittest


class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


def dfs(root, target):

    if root == target:
        return True

    if root.left:
        if dfs(root.left, target):
            return True

    if root.right:
        if dfs(root.right, target):
            return True


def get_common_ancestor(parent, root, p, q):
    if not root:
        return None

    if dfs(root, p) != dfs(root, q):
        return parent

    return get_common_ancestor(root, root.left, p, q) or get_common_ancestor(root, root.right, p, q)


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

        node = get_common_ancestor(None, head, head.right, head.left)
        self.assertEqual(node.value, head.value)

        node = get_common_ancestor(None, head, head.right.right, head.right)
        self.assertEqual(node.value, head.right.value)

        node = get_common_ancestor(None, head, head.right.left, head.right.right)
        self.assertEqual(node.value, head.right.value)


if __name__ == '__main__':
    unittest.main()
