import unittest


def get_build_dfs(g, stack):
    visited = [False] * len(g.nodes)
    for i in range(len(g.nodes)):
        if not depth_first_search(g, i, stack, visited):
            return False
    return True


def depth_first_search(g, s, stack, visited):

    if visited[s] is None:
        return False

    if visited[s] is False:
        visited[s] = None
        for i in range(len(g.nodes)):
            if g.edges[s][i] == 1:
                if not depth_first_search(g, i, stack, visited):
                    return False

        stack.append(s)
        visited[s] = True

    return True


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
        g = Graph(7)
        g.add_directed_edge_unweighted(0, 1)
        g.add_directed_edge_unweighted(0, 2)
        g.add_directed_edge_unweighted(1, 3)
        g.add_directed_edge_unweighted(2, 3)
        g.add_directed_edge_unweighted(0, 3)
        g.add_directed_edge_unweighted(3, 4)
        g.add_directed_edge_unweighted(2, 4)
        g.add_directed_edge_unweighted(5, 6)
        stack = []
        self.assertTrue(get_build_dfs(g, stack))
        print(stack)


if __name__ == '__main__':
    unittest.main()
