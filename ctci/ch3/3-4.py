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


class Queue:
    def __init__(self):
        self.stack_one = Stack()
        self.stack_two = Stack()
        self.size = 0

    def enqueue(self, value):
        self.stack_one.push(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            current_val = None

            while not self.stack_one.is_empty:
                current_val = self.stack_one.pop()
                self.stack_two.push(current_val)

            self.stack_two.pop()

            while not self.stack_two.is_empty:
                self.stack_one.push(self.stack_two.pop())

            return current_val


class TestSolution(unittest.TestCase):
    def test_queue(self):
        queue = Queue()
        queue.enqueue(5)
        self.assertEqual(queue.dequeue(), 5)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)
        self.assertEqual(queue.dequeue(), 5)


if __name__ == '__main__':
    unittest.main()
