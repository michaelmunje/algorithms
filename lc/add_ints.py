# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        current_node = self
        string_rep = ''
        while current_node:
            string_rep += str(current_node.val) + '-'
            current_node = current_node.next
        return string_rep[:-1]


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry_over = 0
    sum_val = None
    current_l1 = l1
    current_l2 = l2
    head = None
    current_l3 = None
    first = True
    while current_l1 or current_l2 or carry_over == 1:
        if current_l1 and current_l2:
            sum_val = current_l1.val + current_l2.val + carry_over
        elif current_l1:
            sum_val = current_l1.val + carry_over
        elif current_l2:
            sum_val = current_l2.val + carry_over
        elif carry_over == 1:
            sum_val = carry_over
        if sum_val >= 10:
            sum_val = sum_val % 10
            carry_over = 1
        else:
            carry_over = 0

        if first:
            head = ListNode(sum_val)
            current_l3 = head
            first = False
        else:
            current_l3.next = ListNode(sum_val)
            current_l3 = current_l3.next

        if current_l1:
            current_l1 = current_l1.next
        if current_l2:
            current_l2 = current_l2.next

    return head


l1 = ListNode(2)
l1.next = ListNode(8)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(5)

l2 = ListNode(5)
l2.next = ListNode(4)

print(l1)
print(l2)

print(addTwoNumbers(l1, l2))

l1 = ListNode(5)
l2 = ListNode(5)
print(addTwoNumbers(l1, l2))



