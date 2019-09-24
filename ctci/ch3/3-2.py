import unittest


class Stack:
    def __init__(self):
        self.values = []
        self.is_empty = True
        self.size = 0

    def push(self, value):

        if self.is_empty:
            self.values.append((value, value))
        else:
            mini = value if value < self.values[-1][1] else self.values[-1][1]
            self.values.append((value, mini))
        self.size += 1
        self.is_empty = False

    def pop(self):
        if not self.is_empty:
            return self.values.pop()[0]
        self.size -= 1
        if self.size == 0:
            self.is_empty = True

    def min(self):
        if not self.is_empty:
            return self.values[-1][1]


class TestSolution(unittest.TestCase):
    def test_stacks(self):
        stack = Stack()  # Size per stack
        stack.push(5)
        self.assertTrue(stack.min(), 5)
        stack.push(3)
        self.assertTrue(stack.min(), 3)
        stack.push(4)
        stack.push(1)
        stack.push(6)
        self.assertTrue(stack.min(), 1)
        self.assertEqual(stack.pop(), 6)
        stack.pop()
        self.assertEqual(stack.min(), 3)


if __name__ == '__main__':
    unittest.main()
