import unittest


class Queue:
    def __init__(self):
        self.elements = []
        self.length = 0

    def dequeue(self):
        if not self.is_empty():
            dequeued_element = self.elements[0]
            self.elements = self.elements[1:]
            self.length -= 1
            return dequeued_element
        else:
            raise Exception('Cannot dequeue empty Queue')

    def enqueue(self, new):
        self.elements.append(new)
        self.length += 1

    def is_empty(self):
        return self.length == 0

    def __repr__(self):
        return str(self.elements)


class TestSolution(unittest.TestCase):

    def test_case1(self):
        queue = Queue()
        queue.enqueue(5)
        self.assertEqual(queue.dequeue(), 5)

    def test_case2(self):
        queue = Queue()
        queue.enqueue(5)
        queue.enqueue(20)
        queue.enqueue('hi')
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.dequeue(), 20)
        self.assertEqual(queue.dequeue(), 'hi')

    def test_case3(self):
        queue = Queue()
        with self.assertRaises(Exception):
            queue.dequeue()


if __name__ == '__main__':
    unittest.main()