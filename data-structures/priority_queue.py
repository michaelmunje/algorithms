import unittest


class PQueue:
    def __init__(self):
        self.elements = []
        self.length = 0

    def dequeue(self):
        if not self.__is_empty():
            dequeued_element, _ = self.elements[0]
            self.elements = self.elements[1:]
            self.length -= 1
            return dequeued_element
        else:
            raise Exception('Cannot dequeue empty Queue')

    def enqueue(self, new, priority):
        if not self.__is_empty():
            for i in range(len(self.elements) + 1):
                if i == len(self.elements):
                    self.elements.append((new, priority))
                    self.length += 1
                    return
                else:
                    _, curr_priority = self.elements[i]
                    if priority < curr_priority:
                        self.elements = self.elements[:i] + [(new, priority)] + self.elements[i:]
                        self.length += 1
                        return

        self.elements.append((new, priority))
        self.length += 1

    def __repr__(self):
        return str([x for x, _ in self.elements])

    def __is_empty(self):
        return self.length == 0


class TestSolution(unittest.TestCase):

    def test_case1(self):
        pq = PQueue()
        pq.enqueue(5, 1)
        self.assertEqual(pq.dequeue(), 5)

    def test_case2(self):
        pq = PQueue()
        pq.enqueue(5, 1)
        pq.enqueue(20, 2)
        pq.enqueue('hi', 3)

        self.assertEqual(pq.dequeue(), 5)
        self.assertEqual(pq.dequeue(), 20)
        self.assertEqual(pq.dequeue(), 'hi')

    def test_case3(self):
        pq = PQueue()
        with self.assertRaises(Exception):
            pq.dequeue()

    def test_case4(self):
        pq = PQueue()
        pq.enqueue(5, 1)
        pq.enqueue(20, 2)
        pq.enqueue('hi', 1)

        self.assertEqual(pq.dequeue(), 5)
        self.assertEqual(pq.dequeue(), 'hi')
        self.assertEqual(pq.dequeue(), 20)

    def test_case5(self):
        pq = PQueue()
        pq.enqueue(5, 1)
        pq.enqueue(20, 2)
        pq.enqueue('hi', 1)

        self.assertEqual(str(pq), '[5, \'hi\', 20]')

    def test_case6(self):
        pq = PQueue()
        pq.enqueue(5, 1)
        pq.enqueue(20, 2)
        pq.enqueue('hi', 3)

        self.assertEqual(str(pq), '[5, 20, \'hi\']')


if __name__ == '__main__':
    unittest.main()