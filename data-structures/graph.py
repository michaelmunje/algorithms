import unittest


def dfs(g, s, d):
    visited = [False] * len(g.nodes)
    if depth_first_search(g, s, d, visited) is True:
        return True
    else:
        return False


def depth_first_search(g, s, d, visited):
    visited[s] = True
    for i in range(len(g.nodes)):
        if g.edges[s][i] == 1 and visited[i] is False:
            if d == i:
                return True
            else:
                return depth_first_search(g, i, d, visited)


class UnweightedGraph:
    def __init__(self, size):
        self.edges = [[0] * size] * size
        self.nodes = [''] * size

    def add_undirected_edge(self, s, d):
        self.add_directed_edge(s, d)
        self.add_directed_edge(d, s)

    def add_directed_edge(self, s, d):
        self.edges[s][d] = 1

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
        g = UnweightedGraph(6)
        g.add_directed_edge(0, 1)
        g.add_directed_edge(1, 2)
        g.add_directed_edge(1, 3)
        self.assertTrue(dfs(g, 0, 1))
        self.assertTrue(dfs(g, 0, 3))
        self.assertFalse(dfs(g, 0, 4))
        g.add_directed_edge(4, 5)
        g.add_directed_edge(3, 4)
        self.assertTrue(dfs(g, 0, 4))
        self.assertTrue(dfs(g, 0, 5))



if __name__ == '__main__':
    unittest.main()