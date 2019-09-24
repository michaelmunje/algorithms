import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class StackFromArrays:
    def __init__(self, size):
        self.array = [None] * size * 3
        self.size = size * 3
        self.stackOneEmpty = True
        self.stackTwoEmpty = True
        self.stackThreeEmpty = True
        self.stackOneSize = 0
        self.stackTwoSize = 0
        self.stackThreeSize = 0

    def push_one(self, value):
        if not self.stackOneSize == self.size/3:
            self.array[self.stackOneSize] = value
            self.stackOneSize += 1
            self.stackOneEmpty = False

    def push_two(self, value):
        if not self.stackTwoSize == self.size/3:
            self.array[self.stackTwoSize + self.size//3] = value
            self.stackTwoSize += 1
            self.stackTwoEmpty = False

    def push_three(self, value):
        if not self.stackThreeSize == self.size/3:
            self.array[self.stackThreeSize + 2 * self.size//3] = value
            self.stackThreeSize += 1
            self.stackThreeEmpty = False

    def pop_one(self):
        if not self.stackOneEmpty:
            self.stackOneSize -= 1
            if self.stackOneSize == 0:
                self.stackOneEmpty = True
            return self.array[self.stackOneSize]

    def pop_two(self):
        if not self.stackTwoEmpty:
            self.stackTwoSize -= 1
            if self.stackTwoSize == 0:
                self.stackTwoEmpty = True
            return self.array[self.stackTwoSize + self.size//3]

    def pop_three(self):
        if not self.stackThreeEmpty:
            if self.stackThreeSize == 0:
                self.stackThreeEmpty = True
            self.stackThreeSize -= 1
            return self.array[self.stackThreeSize + (2*self.size)//3]


class TestSolution(unittest.TestCase):
    def test_stacks(self):
        stacks = StackFromArrays(5)  # Size per stack
        stacks.push_one(1)
        stacks.push_two(2)
        stacks.push_three(5)
        self.assertEqual(stacks.pop_one(), 1)
        self.assertEqual(stacks.pop_two(), 2)
        self.assertEqual(stacks.pop_three(), 5)
        stacks.push_two(100)
        stacks.push_two(99)
        stacks.push_three(87)
        stacks.push_three(94)
        stacks.push_one(21)
        stacks.push_one(25)
        self.assertEqual(stacks.pop_two(), 99)
        self.assertEqual(stacks.pop_three(), 94)
        self.assertEqual(stacks.pop_three(), 87)
        self.assertEqual(stacks.pop_one(), 25)
        self.assertEqual(stacks.pop_two(), 100)
        self.assertEqual(stacks.pop_one(), 21)


if __name__ == '__main__':
    unittest.main()
