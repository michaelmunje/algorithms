import unittest


def is_unique_bitwise(s):  # O(n)
    checker = 0
    for c in s:
        val = ord(c) - ord('a')
        if checker & (1 << val) > 0:
            return False
        checker = checker | (1 << val)
    return True


def is_unique_sorted(s):  # O(nlogn)
    s = sorted(s)
    if not s:
        return True
    prev = s[0]
    for i in range(1, len(s)):
        if s[i] == prev:
            return False
        prev = s[i]
    return True


def is_unique(s):  # O(n)
    chars = dict()
    for ch in s:
        if ch in chars:
            if chars[ch] == 1:
                return False
        chars[ch] = 1
    return True


def is_unique_no_ds(s):  # O(n^2)
    for i, ch1 in enumerate(s):
        for ch2 in s[i+1:]:
            if ch1 == ch2:
                return False
    return True


class TestSolution(unittest.TestCase):
    def test_unique_strings(self):
        self.assertTrue(is_unique("abcdefg"))
        self.assertTrue(is_unique("man"))
        self.assertTrue(is_unique(""))

    def test_non_unique_strings(self):
        self.assertFalse(is_unique("nascar"))
        self.assertFalse(is_unique("mansion"))

    def test_unique_strings_no_ds(self):
        self.assertTrue(is_unique_no_ds("abcdefg"))
        self.assertTrue(is_unique_no_ds("man"))
        self.assertTrue(is_unique_no_ds(""))

    def test_non_unique_strings_no_ds(self):
        self.assertFalse(is_unique_no_ds("nascar"))
        self.assertFalse(is_unique_no_ds("mansion"))

    def test_unique_strings_bitwise(self):
        self.assertTrue(is_unique_bitwise("abcdefg"))
        self.assertTrue(is_unique_bitwise("man"))
        self.assertTrue(is_unique_bitwise(""))

    def test_non_unique_strings_bitwise(self):
        self.assertFalse(is_unique_bitwise("nascar"))
        self.assertFalse(is_unique_bitwise("mansion"))

    def test_unique_strings_sorted(self):
        self.assertTrue(is_unique_sorted("abcdefg"))
        self.assertTrue(is_unique_sorted("man"))
        self.assertTrue(is_unique_sorted(""))

    def test_non_unique_strings_sorted(self):
        self.assertFalse(is_unique_sorted("nascar"))
        self.assertFalse(is_unique_sorted("mansion"))


if __name__ == '__main__':
    unittest.main()
