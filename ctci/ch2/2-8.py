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


def linked_lists_intersect(l1, l2):  # O(n)

    current_a = l1
    current_b = l2
    visited_nodes = dict()

    while current_a or current_b:

        if current_a:
            if current_a in visited_nodes:
                return current_a
            else:
                visited_nodes[current_a] = 1
            current_a = current_a.next

        if current_b:
            if current_b in visited_nodes:
                return current_b
            else:
                visited_nodes[current_b] = 1
            current_b = current_b.next


class TestSolution(unittest.TestCase):
    def test_cycles(self):

        head1 = list_to_linked_list([7, 1, 6])
        head2 = list_to_linked_list([2, 7, 1, 6])

        self.assertFalse(linked_lists_intersect(head1, head2))

        head3 = list_to_linked_list([0, 1, 2])

        head1.next.next.next = head3

        head2.next.next = head3

        self.assertTrue(linked_lists_intersect(head1, head2))

        head1.next.next.next = head2

        self.assertTrue(linked_lists_intersect(head1, head2))


if __name__ == '__main__':
    unittest.main()
