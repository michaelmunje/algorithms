import unittest


def set_zeroes(matrix):
    marked_rows = []
    marked_cols = []
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                marked_rows.append(i)
                marked_cols.append(j)

    for i in range(m):
        for j in range(n):
            if i in marked_rows or j in marked_cols:
                matrix[i][j] = 0

    return matrix


class TestSolution(unittest.TestCase):
    def test_set_zeroes(self):
        self.assertEqual(set_zeroes([[1,1,1],[1,0,1],[1,1,1]]), [[1,0,1],[0,0,0],[1,0,1]])


if __name__ == '__main__':
    unittest.main()