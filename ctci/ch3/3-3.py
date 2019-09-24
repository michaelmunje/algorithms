import unittest


class SetOfStacks:
    def __init__(self, size):
        self.stacks = [[]]
        self.current_stack = 0
        self.is_empty = True
        self.current_size = 0
        self.max_size = size

    def push(self, value):
        if self.current_size == self.max_size:
            self.stacks.append([])
            self.current_stack += 1
            self.current_size = 0
        self.stacks[self.current_stack].append(value)
        self.current_size += 1
        self.is_empty = False

    def pop(self):
        if not self.is_empty:
            val = self.stacks[self.current_stack].pop()
            self.current_size -= 1
            if self.current_size == 0:
                if self.current_stack == 0:
                    self.is_empty = True
                else:
                    self.current_stack -= 1
                    self.stacks.pop()
            return val

    def pop_ith(self, i):
        if i <= self.current_stack:
            if i < self.current_stack:
                val = self.stacks[i].pop()
                self.current_size -= 1
                for j in range(i, self.current_stack):
                    self.stacks[j].append(self.stacks[j+1][0])
                    self.stacks[j+1] = self.stacks[j+1][1:]
                if self.current_stack - i == 1:
                    if self.current_size == 0:
                        self.stacks.pop()
                        self.current_stack -= 1
                        self.current_size = self.max_size
                return val
            else:
                return self.pop()


class TestSolution(unittest.TestCase):
    def test_stacks(self):
        stack = SetOfStacks(2)  # Size per stack
        stack.push(5)
        self.assertTrue(stack.pop(), 5)
        stack.push(3)
        stack.push(4)
        stack.push(1)
        stack.push(6)
        self.assertTrue(stack.pop(), 6)
        stack.push(7)
        stack.push(8)
        self.assertEqual(stack.pop_ith(1), 7)
        self.assertEqual(stack.pop_ith(0), 4)
        self.assertEqual(stack.pop(), 8)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), 3)


if __name__ == '__main__':
    unittest.main()
