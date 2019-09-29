import unittest


def bit_insertion(a, b, i, j):
    mask = ~0
    mask <<= j
    mask |= (1 << i) - 1
    return (a & mask) | (b << i)


class TestSolution(unittest.TestCase):
    def test_stacks(self):

        a = 2048
        b = 19
        self.assertEqual(bit_insertion(a, b, 2, 6), 2124)

        a = 2057
        b = 19
        self.assertEqual(bit_insertion(a, b, 2, 6), 2125)

        a = 2049
        b = 19
        self.assertEqual(bit_insertion(a, b, 2, 6), 2125)


if __name__ == '__main__':
    unittest.main()
