import unittest


def dfs(g, s, d):
    visited = [False] * len(g.nodes)
    depth_first_search(g, s, d, visited)
    return visited[d]


def depth_first_search(g, s, d, visited):
    visited[s] = True
    for i in range(len(g.nodes)):
        if g.edges[s][i] == 1 and visited[i] is False:
            depth_first_search(g, i, d, visited)


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
    def test_stacks(self):
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


if __name__ == '__main__':
    unittest.main()
