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


def linked_list_list(head):   # Convenience function to get list of all ll values
    current_node = head
    ll_list = []
    while current_node:
        ll_list.append(current_node.val)
        current_node = current_node.next
    return ll_list


def find_kth_to_last(head, k):  # O(n)
    if not head:
        return head

    behind_node = head
    current_node = behind_node
    current_distance = 0

    while current_node:
        if current_distance == k:
            behind_node = behind_node.next
        else:
            current_distance += 1
        current_node = current_node.next
    return behind_node


class TestSolution(unittest.TestCase):
    def test_kth_to_last(self):
        head = list_to_linked_list([1, 2, 3, 4, 5])
        self.assertEqual(find_kth_to_last(head, 4).val, 2)
        self.assertEqual(find_kth_to_last(head, 2).val, 4)
        self.assertNotEqual(find_kth_to_last(head, 3).val, 4)


if __name__ == '__main__':
    unittest.main()
