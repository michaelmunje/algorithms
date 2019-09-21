import unittest


class PriorityItem:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class Heap:  # Min heap
    def __init__(self):
        self.values = []

    def remove_min(self):
        old_max = self.values[0]
        if len(self.values) > 1:
            self.values[0] = self.values[-1]
            self.values.pop()

        i = 0

        while 2*i+1 < len(self.values):

            swap_i = 2*i+1

            if 2*i + 2 < len(self.values):
                if min(self.values[2*i+1].priority, self.values[2*i+2].priority) >= self.values[i].priority:
                    break

                if self.values[2*i+2].priority < self.values[2*i+1].priority:
                    swap_i += 1
            else:
                if self.values[2*i+1].priority >= self.values[i].priority:
                    break

            tmp = self.values[i]
            self.values[i] = self.values[swap_i]
            self.values[swap_i] = tmp
            i = swap_i

        return old_max.value

    def add_node(self, item):
        self.values.append(item)
        current_i = len(self.values) - 1
        if current_i == 0:
            return

        while current_i > 0 and self.values[current_i].priority < self.values[(current_i - 1) // 2].priority:
            tmp = self.values[current_i]
            self.values[current_i] = self.values[(current_i - 1) // 2]
            self.values[(current_i - 1) // 2] = tmp
            current_i = (current_i - 1) // 2

    def __repr__(self):
        return str([val.value for val in self.values])


class PQueue:
    def __init__(self):
        self.heap = Heap()
        self.length = 0

    def dequeue(self):
        if not self.__is_empty():
            self.length -= 1
            return self.heap.remove_min()
        else:
            raise Exception('Cannot dequeue empty Queue')

    def enqueue(self, new, priority):
        self.heap.add_node(PriorityItem(new, priority))
        self.length += 1

    def __repr__(self):
        return str(self.heap)

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
        pq.enqueue('hi', 3)

        self.assertEqual(str(pq), '[5, 20, \'hi\']')


if __name__ == '__main__':
    unittest.main()