import unittest


class Stack:
    def __init__(self):
        self.values = []
        self.is_empty = True
        self.size = 0

    def push(self, value):
        self.values.append(value)
        self.size += 1
        self.is_empty = False

    def pop(self):
        if not self.is_empty:
            self.size -= 1
            if self.size == 0:
                self.is_empty = True
            return self.values.pop()

    def peek(self):
        if not self.is_empty:
            return self.values[-1]


def sort_stack(stack):
    temp_stack = Stack()

    while not stack.is_empty:
        temp = stack.pop()
        while not temp_stack.is_empty and temp_stack.peek() > temp:
            stack.push(temp_stack.pop())
        temp_stack.push(temp)

    while not temp_stack.is_empty:
        stack.push(temp_stack.pop())

    return stack


class TestSolution(unittest.TestCase):
    def test_queue(self):
        stack = Stack()
        stack.push(1)
        stack.push(9)
        stack.push(7)
        stack.push(3)
        stack.push(5)
        self.assertEqual(sort_stack(stack).values, [9, 7, 5, 3, 1])


if __name__ == '__main__':
    unittest.main()
