import unittest


def binary_rep_for_float(a):
    if a == 1 or a == 0:
        return None

    binary_rep = '.'
    current_comp = 1/2

    while a > 1e-9:
        if len(binary_rep) > 32:
            return None
        if a >= current_comp:
            binary_rep += '1'
            a -= current_comp
        else:
            binary_rep += '0'
        print(a)
        current_comp /= 2

    return binary_rep


class TestSolution(unittest.TestCase):
    def test_stacks(self):
        print(binary_rep_for_float(0.05))


if __name__ == '__main__':
    unittest.main()
