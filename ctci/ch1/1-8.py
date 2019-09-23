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


def set_zeroes_optimized(matrix):
    is_col_zero = False
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        if matrix[i][0] == 0:
            is_col_zero = True
        for j in range(1, c):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, r):
        for j in range(1, c):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        for j in range(c):
            matrix[0][j] = 0

    if is_col_zero:
        for i in range(r):
            matrix[i][0] = 0

    return matrix


class TestSolution(unittest.TestCase):
    def test_set_zeroes(self):
        self.assertEqual(set_zeroes([[1,1,1],[1,0,1],[1,1,1]]), [[1,0,1],[0,0,0],[1,0,1]])
        self.assertEqual(set_zeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]), [[0,0,0,0],[0,4,5,0],[0,3,1,0]])
        self.assertEqual(set_zeroes([[1,1,1],[0,1,2]]), [[0,1,1],[0,0,0]])

    def test_set_zeroes_opt(self):
        self.assertEqual(set_zeroes_optimized([[1,1,1],[1,0,1],[1,1,1]]), [[1,0,1],[0,0,0],[1,0,1]])
        self.assertEqual(set_zeroes_optimized([[0,1,2,0],[3,4,5,2],[1,3,1,5]]), [[0,0,0,0],[0,4,5,0],[0,3,1,0]])
        self.assertEqual(set_zeroes_optimized([[1,1,1],[0,1,2]]), [[0,1,1],[0,0,0]])


if __name__ == '__main__':
    unittest.main()