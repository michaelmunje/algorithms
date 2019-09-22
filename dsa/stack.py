import unittest


class Stack:
    def __init__(self):
        self.elements = []
        self.length = 0

    def pop(self):
        if not self.is_empty():
            popped_element = self.elements[-1]
            self.elements = self.elements[:-1]
            self.length -= 1
            return popped_element
        else:
            raise Exception('Cannot pop empty Stack')

    def push(self, new):
        self.elements.append(new)
        self.length += 1

    def is_empty(self):
        return self.length == 0


class TestSolution(unittest.TestCase):

    def test_case1(self):
        stack = Stack()
        stack.push(5)
        self.assertEqual(stack.pop(), 5)

    def test_case2(self):
        stack = Stack()
        stack.push(5)
        stack.push(20)
        stack.push('hi')
        self.assertEqual(stack.pop(), 'hi')
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 5)

    def test_case3(self):
        stack = Stack()
        with self.assertRaises(Exception):
            stack.pop()


if __name__ == '__main__':
    unittest.main()