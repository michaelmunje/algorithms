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


def partition_list(head, value):  # O(n)
    prev_node = head
    current_node = prev_node.next
    right_partition = right_partition_head = None
    first = True
    while current_node:
        if current_node.val >= value:

            if first:
                right_partition_head = Node(current_node.val)
                right_partition = right_partition_head
                first = False
            else:
                right_partition.next = Node(current_node.val)
                right_partition = right_partition.next

            prev_node.next = current_node.next
        else:
            prev_node = current_node

        current_node = current_node.next
    prev_node.next = right_partition_head
    return head


class TestSolution(unittest.TestCase):
    def test_node_removal(self):
        head = list_to_linked_list([1, 6, 2, 3, 7, 2, 4, 5])
        self.assertEqual(linked_list_list(partition_list(head, 5)), [1, 2, 3, 2, 4, 6, 7, 5])


if __name__ == '__main__':
    unittest.main()
