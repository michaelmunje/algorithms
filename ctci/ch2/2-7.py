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


def linked_list_has_cycle(head):  # O(n)

    current_node = head
    visited_nodes = dict()

    while current_node:

        if current_node in visited_nodes:
            return True
        else:
            visited_nodes[current_node] = 1

        current_node = current_node.next

    return False


class TestSolution(unittest.TestCase):
    def test_cycles(self):

        head = list_to_linked_list([7, 1, 6])
        self.assertFalse(linked_list_has_cycle(head))

        head.next.next.next = head
        self.assertTrue(linked_list_has_cycle(head))

        head = list_to_linked_list([7, 1, 6, 2, 5])
        self.assertFalse(linked_list_has_cycle(head))

        head.next.next.next = head.next
        self.assertTrue(linked_list_has_cycle(head))


if __name__ == '__main__':
    unittest.main()
