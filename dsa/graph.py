import unittest
from queue import Queue
from priority_queue import PQueue
import sys


def dfs(g, s, d):
    visited = [False] * len(g.nodes)
    depth_first_search(g, s, d, visited)
    return visited[d]


def depth_first_search(g, s, d, visited):
    visited[s] = True
    for i in range(len(g.nodes)):
        if g.edges[s][i] == 1 and visited[i] is False:
            depth_first_search(g, i, d, visited)


def breadth_first_search(g, s, d):
    visited = [False] * len(g.nodes)
    q = Queue()
    q.enqueue(s)
    while not q.is_empty():
        current = q.dequeue()
        visited[current] = True
        for i in range(len(g.nodes)):
            if g.edges[current][i] == 1 and visited[i] is False:
                if d == i:
                    return True
                else:
                    q.enqueue(i)
    return False


def shortest_path(g, s, d):
    dist = [sys.maxsize] * len(g.nodes)
    prev = [None] * len(g.nodes)
    dist[s] = 0

    visited = [False] * len(g.nodes)
    pq = PQueue()
    pq.enqueue(s, 0)

    while not pq.is_empty():
        current, weight = pq.dequeue()
        visited[current] = True
        for i in range(len(g.nodes)):
            if g.edges[current][i] > 0:
                current_dist = g.edges[current][i] + dist[current]

                if current_dist < dist[i]:
                    dist[i] = current_dist
                    prev[i] = current

                if not visited[i]:
                    pq.enqueue(i, current_dist)

    return dist[d]


class Graph:
    def __init__(self, size):
        self.edges = [0] * size
        for i in range(size):
            self.edges[i] = [0] * size

        self.nodes = [''] * size

    def add_undirected_edge(self, s, d, m):
        self.add_directed_edge(s, d, m)
        self.add_directed_edge(d, s, m)

    def add_directed_edge_unweighted(self, s, d):
        self.edges[s][d] = 1

    def add_directed_edge(self, s, d, mag):
        self.edges[s][d] = mag

    def remove_undirected_edge(self, s, d):
        self.remove_directed_edge(s, d)
        self.remove_directed_edge(d, s)

    def remove_directed_edge(self, s, d):
        self.edges[s][d] = 0

    def __repr__(self):
        return str(self.heap)

    def __is_empty(self):
        return self.length == 0


class TestSolution(unittest.TestCase):

    def test_case1(self):
        g = Graph(6)
        g.add_directed_edge_unweighted(0, 1)
        g.add_directed_edge_unweighted(1, 2)
        g.add_directed_edge_unweighted(1, 3)
        self.assertTrue(dfs(g, 0, 1))
        self.assertTrue(dfs(g, 0, 3))
        self.assertFalse(dfs(g, 0, 4))
        g.add_directed_edge_unweighted(4, 5)
        g.add_directed_edge_unweighted(3, 4)
        self.assertTrue(dfs(g, 0, 4))
        self.assertTrue(dfs(g, 0, 5))

    def test_case2(self):
        g = Graph(6)
        g.add_directed_edge_unweighted(0, 1)
        g.add_directed_edge_unweighted(1, 2)
        g.add_directed_edge_unweighted(1, 3)
        self.assertTrue(breadth_first_search(g, 0, 1))
        self.assertTrue(breadth_first_search(g, 0, 3))
        self.assertFalse(breadth_first_search(g, 0, 4))
        g.add_directed_edge_unweighted(4, 5)
        g.add_directed_edge_unweighted(3, 4)
        self.assertTrue(breadth_first_search(g, 0, 4))
        self.assertTrue(breadth_first_search(g, 0, 5))

    def test_case3(self):
        g = Graph(6)
        g.add_directed_edge(0, 1, 2)
        g.add_directed_edge(0, 2, 7)
        g.add_directed_edge(1, 3, 2)
        g.add_directed_edge(1, 3, 2)
        g.add_directed_edge(1, 2, 3)
        g.add_directed_edge(2, 4, 1)
        g.add_directed_edge(4, 5, 1)
        g.add_directed_edge(2, 3, 5)
        g.add_directed_edge(3, 5, 6)
        self.assertEqual(shortest_path(g, 0, 5), 7)

    def test_case4(self):
        g = Graph(4)
        g.add_directed_edge(0, 1, 1)
        g.add_directed_edge(0, 2, 7)
        g.add_directed_edge(1, 2, 1)
        g.add_directed_edge(2, 0, 2)
        g.add_directed_edge(2, 3, 1)
        g.add_directed_edge(1, 3, 8)
        self.assertEqual(shortest_path(g, 0, 3), 3)


if __name__ == '__main__':
    unittest.main()