import unittest


def check_rotation(a, b):
    return len(a) == len(b) and b in a + a


def check_rotation_2(A, B):
    if len(A) != len(B):
        return False

    if A == B:
        return True

    for i in range(len(A)):
        if A[i:] + A[:i] == B:
            return True
    return False


class TestSolution(unittest.TestCase):
    def test_rotation(self):
        self.assertTrue(check_rotation('waterbottle', 'erbottlewat'))
        self.assertTrue(check_rotation('car', 'rca'))

    def test_no_rotation(self):
        self.assertFalse(check_rotation('waterbottler', 'erbottlewata'))
        self.assertFalse(check_rotation('cars', 'rca'))

    def test_rotation_2(self):
        self.assertTrue(check_rotation_2('waterbottle', 'erbottlewat'))
        self.assertTrue(check_rotation_2('car', 'rca'))

    def test_no_rotation_2(self):
        self.assertFalse(check_rotation_2('waterbottler', 'erbottlewata'))
        self.assertFalse(check_rotation_2('cars', 'rca'))


if __name__ == '__main__':
    unittest.main()
