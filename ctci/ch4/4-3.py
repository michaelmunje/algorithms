import unittest


class Queue:
    def __init__(self):
        self.elements = []
        self.length = 0

    def dequeue(self):
        if not self.is_empty():
            dequeued_element = self.elements[0]
            self.elements = self.elements[1:]
            self.length -= 1
            return dequeued_element
        else:
            raise Exception('Cannot dequeue empty Queue')

    def enqueue(self, new):
        self.elements.append(new)
        self.length += 1

    def is_empty(self):
        return self.length == 0

    def __repr__(self):
        return str(self.elements)


class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


def bst_to_lists_level_by_level(head):   # assumes a complete tree. Otherwise would need to keep track of # of children
    q = Queue()
    q.enqueue(head)
    i = 0
    current_level = 0
    values = [[]]

    while not q.is_empty():
        current_node = q.dequeue()
        if current_node.value:
            values[current_level].append(current_node.value)
            if current_node.left:
                q.enqueue(current_node.left)
            if current_node.right:
                q.enqueue(current_node.right)
            i += 1
            if i == 2**current_level:
                current_level += 1
                values.append([])
                i = 0

    return values


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
        self.assertEqual(bst_to_lists_level_by_level(head), [[5], [3, 8], [2, 4, 7, 9], [1, 6]])
        a = [1, 2, 3, 4]
        head = list_to_bst(a)
        self.assertEqual(bst_to_lists_level_by_level(head), [[3], [2, 4], [1]])


if __name__ == '__main__':
    unittest.main()
