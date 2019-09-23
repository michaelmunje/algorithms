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


def add_linked_lists_backwards(head1, head2):  # O(n)

    sum_node = sum_head = None
    current_node = head1
    other_node = head2

    carry_over = 0
    first = True

    while current_node or other_node:

        current_sum = carry_over

        if current_node:
            current_sum += current_node.val
            current_node = current_node.next

        if other_node:
            current_sum += other_node.val
            other_node = other_node.next

        carry_over = 1 if current_sum >= 10 else 0

        if first:
            sum_head = Node(current_sum % 10)
            sum_node = sum_head
            first = False
        else:
            sum_node.next = Node(current_sum % 10)
            sum_node = sum_node.next

    if carry_over > 0:
        sum_node.next = Node(carry_over)

    return sum_head


def add_linked_lists_forwards(l1, l2):  # O(n)
    s1 = []
    s2 = []
    current_node = l1
    while current_node:
        s1.append(current_node.val)
        current_node = current_node.next
    current_node = l2
    while current_node:
        s2.append(current_node.val)
        current_node = current_node.next

    carry_over = 0
    total_sum = []

    for i in range(max(len(s1), len(s2))):

        if i < len(s1) and i < len(s2):
            new_sum = s1[-1 - i] + s2[-1 - i] + carry_over
        elif i < len(s1):
            new_sum = s1[-1 - i] + carry_over
        else:
            new_sum = s2[-1 - i] + carry_over

        total_sum.append(new_sum % 10)

        if new_sum >= 10:
            carry_over = 1
        else:
            carry_over = 0

    if carry_over == 1:
        total_sum.append(1)

    head = Node(total_sum[-1])
    current_node = head
    for i in range(1, len(total_sum)):
        current_node.next = Node(total_sum[-1 - i])
        current_node = current_node.next
    return head


class TestSolution(unittest.TestCase):
    def test_adding_backwards(self):
        head = list_to_linked_list([7, 1, 6])
        head2 = list_to_linked_list([5, 9, 2])
        self.assertEqual(linked_list_list(add_linked_lists_backwards(head, head2)), [2, 1, 9])
        head = list_to_linked_list([7, 1, 9])
        head2 = list_to_linked_list([5, 9, 1])
        self.assertEqual(linked_list_list(add_linked_lists_backwards(head, head2)), [2, 1, 1, 1])
        head = list_to_linked_list([7, 1, 9])
        head2 = list_to_linked_list([])
        self.assertEqual(linked_list_list(add_linked_lists_backwards(head, head2)), [7, 1, 9])

    def test_adding_forwards(self):
        head = list_to_linked_list([7, 1, 6])
        head2 = list_to_linked_list([5, 9, 2])
        self.assertEqual(linked_list_list(add_linked_lists_forwards(head, head2)), [1, 3, 0, 8])
        head = list_to_linked_list([7, 1, 9])
        head2 = list_to_linked_list([5, 9, 1])
        self.assertEqual(linked_list_list(add_linked_lists_forwards(head, head2)), [1, 3, 1, 0])
        head = list_to_linked_list([7, 1, 9])
        head2 = list_to_linked_list([])
        self.assertEqual(linked_list_list(add_linked_lists_forwards(head, head2)), [7, 1, 9])


if __name__ == '__main__':
    unittest.main()
