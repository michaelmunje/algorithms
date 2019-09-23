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


def linked_list_list(head):   # Convience function to get list of all ll values
    current_node = head
    ll_list = []
    while current_node:
        ll_list.append(current_node.val)
        current_node = current_node.next
    return ll_list


def remove_duplicates(head):
    if not head:
        return head
    values = dict()
    prev_node = head
    values[prev_node.val] = 1
    current_node = prev_node.next
    while current_node:
        if current_node.val in values:
            prev_node.next = current_node.next
        else:
            values[current_node.val] = 1
            prev_node = current_node
        current_node = prev_node.next
    return head


class TestSolution(unittest.TestCase):
    def test_duplicate_removal(self):
        head = list_to_linked_list([1, 2, 3, 4, 5])
        head = remove_duplicates(head)
        self.assertEqual(linked_list_list(head), [1, 2, 3, 4, 5])
        head = list_to_linked_list([1, 2, 3, 4, 2, 5])
        head = remove_duplicates(head)
        self.assertEqual(linked_list_list(head), [1, 2, 3, 4, 5])
        head = list_to_linked_list([1, 1, 2, 3, 4, 2, 5])
        head = remove_duplicates(head)
        self.assertEqual(linked_list_list(head), [1, 2, 3, 4, 5])
        head = list_to_linked_list([1, 1, 3, 3])
        head = remove_duplicates(head)
        self.assertEqual(linked_list_list(head), [1, 3])
        head = list_to_linked_list([1, 1, 2, 3, 4, 2, 3])
        head = remove_duplicates(head)
        self.assertEqual(linked_list_list(head), [1, 2, 3, 4])
        head = list_to_linked_list([1, 1, 1, 1, 1, 1])
        head = remove_duplicates(head)
        self.assertEqual(linked_list_list(head), [1])


if __name__ == '__main__':
    unittest.main()
