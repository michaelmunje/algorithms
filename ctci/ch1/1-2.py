import unittest


def is_permutation(s, p):  # runtime: O(n)
    chars = dict()

    for c in s:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    for c in p:
        if c in chars:
            chars[c] -= 1
        else:
            return False

    for _, value in chars.items():
        if value != 0:
            return False

    return True


def is_permutation_sorted(s, p):
    return sorted(s) == sorted(p)


class TestSolution(unittest.TestCase):
    def test_unique_strings(self):
        self.assertTrue(is_permutation("abc", "cba"))
        self.assertTrue(is_permutation("abc", "acb"))

    def test_non_unique_strings(self):
        self.assertFalse(is_permutation("abc", "cbad"))
        self.assertFalse(is_permutation("abc", "abb"))

    def test_unique_strings_sorted(self):
        self.assertTrue(is_permutation_sorted("abc", "cba"))
        self.assertTrue(is_permutation_sorted("abc", "acb"))

    def test_non_unique_strings_sorted(self):
        self.assertFalse(is_permutation_sorted("abc", "cbad"))
        self.assertFalse(is_permutation_sorted("abc", "abb"))


if __name__ == '__main__':
    unittest.main()