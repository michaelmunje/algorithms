import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def list_to_linked_list(a):
    if not a:
        return None
    else:
        current_node = head = Node(a[0])
        for i in range(1, len(a)):
            current_node.next = Node(a[i])
            current_node = current_node.next
        return head


def linked_list_list(head):  # Convenience function to get list of all ll values
    current_node = head
    ll_list = []
    while current_node:
        ll_list.append(current_node.val)
        current_node = current_node.next
    return ll_list


def remove_middle_node(node):  # O(n)
    if node.next:
        node.val = node.next.val
        node.next = node.next.next
        return node


class TestSolution(unittest.TestCase):
    def test_node_removal(self):
        head = list_to_linked_list([1, 2, 3, 4, 5])
        head.next.next = remove_middle_node(head.next.next)
        self.assertEqual(linked_list_list(head), [1, 2, 4, 5])


if __name__ == '__main__':
    unittest.main()
