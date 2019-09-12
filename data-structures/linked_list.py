import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.__length = 0

    def append(self, value_to_add):
        if self.__length > 0:
            self.tail.next = Node(value_to_add)
            self.tail = self.tail.next
        else:
            self.head = Node(value_to_add)
            self.tail = self.head
        self.__length += 1

    def remove_end(self):
        if self.__length == 0:
            raise Exception('Cannot remove end from empty Linked List')
        elif self.__length == 1:
            self.head = None
        else:
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next
            self.tail = current_node
            current_node.next = None

        self.__length -= 1

    def search(self, value):
        current_node = self.head
        i = 0
        while current_node:
            if current_node.value == value:
                return i
            else:
                i += 1
                current_node = current_node.next
        return None

    def remove(self, value):
        current_node = self.head
        if not current_node:
            return False
        if current_node.value == value:
            self.head = current_node.next
            if self.__length == 2:
                self.tail = current_node.next
            self.__length -= 1
            return True
        previous_node = current_node
        current_node = current_node.next
        while current_node:
            if current_node.value == value:
                previous_node.next = current_node.next
                if current_node.next is None:
                    self.tail = previous_node
                self.__length -= 1
                return True
            else:
                previous_node = current_node
                current_node = current_node.next
        return False

    def __repr__(self):
        string_representation = ''
        if not self.head:
            return string_representation
        current_node = self.head
        while current_node:
            string_representation += str(current_node.value) + '-'
            current_node = current_node.next
        return string_representation[:-1]


class TestSolution(unittest.TestCase):

    def test_case1(self):
        ll = LinkedList()
        ll.append(5)
        ll.append(3)
        ll.remove(3)
        ll.append(4)
        ll.append(2)
        ll.remove_end()
        ll.remove_end()
        ll.remove_end()
        with self.assertRaises(Exception):
            ll.remove_end()

    def test_case2(self):
        ll = LinkedList()
        ll.append(5)
        ll.append(3)
        self.assertEqual(None, ll.search(2))
        self.assertEqual(1, ll.search(3))
        self.assertEqual(0, ll.search(5))

    def test_case3(self):
        ll = LinkedList()
        ll.append(3)
        ll.append(2)
        ll.append(6)
        self.assertTrue(ll.remove(3))
        self.assertFalse(ll.remove(9))
        self.assertTrue(ll.remove(6))

    def test_case4(self):
        ll = LinkedList()
        with self.assertRaises(Exception):
            ll.remove_end()

    def test_case5(self):
        ll = LinkedList()
        ll.append(3)
        ll.append(2)
        ll.append(6)
        self.assertEqual('3-2-6', str(ll))
        ll.remove_end()
        self.assertEqual('3-2', str(ll))
        ll.remove(3)
        self.assertEqual('2', str(ll))


if __name__ == '__main__':
    unittest.main()