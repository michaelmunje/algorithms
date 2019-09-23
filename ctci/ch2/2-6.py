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


def is_linked_list_palindrome(head):  # O(n)

    stack = []

    current_node = head
    length = 0

    while current_node:

        length += 1
        current_node = current_node.next

    current_node = head
    i = 0

    while current_node:

        if i < length // 2:
            stack.append(current_node.val)

        elif i > length // 2 or length % 2 == 0:
            if current_node.val != stack[-1]:
                return False
            stack.pop()

        current_node = current_node.next
        i += 1

    return True


class TestSolution(unittest.TestCase):
    def test_palindrome(self):
        head = list_to_linked_list([7, 1, 6])
        self.assertFalse(is_linked_list_palindrome(head))
        head = list_to_linked_list([1, 0, 1])
        self.assertTrue(is_linked_list_palindrome(head))
        head = list_to_linked_list([1, 0, 0, 1])
        self.assertTrue(is_linked_list_palindrome(head))


if __name__ == '__main__':
    unittest.main()
