import unittest


def isUniqueBitwise(s):
    checker = 0
    for c in s:
        val = ord(c) - ord('a')
        if checker & (1 << val) > 0:
            return False
        checker = checker | (1 << val)
    return True


def is_unique_sorted(s):
    s = sorted(s)
    if not s:
        return True
    prev = s[0]
    for i in range(1, len(s)):
        if s[i] == prev:
            return False
        prev = s[i]
    return True


def isUnique(s):
    chars = dict()
    for i in range(len(s)):
        if s[i] in chars:
            if chars[s[i]] == 1:
                return False
        chars[s[i]] = 1
    return True


def isUniqueNoDs(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


class TestSolution(unittest.TestCase):
    def testUniqueStrings(self):
        self.assertTrue(isUnique("abcdefg"))
        self.assertTrue(isUnique("man"))
        self.assertTrue(isUnique(""))

    def testNonUniqueStrings(self):
        self.assertFalse(isUnique("nascar"))
        self.assertFalse(isUnique("mansion"))

    def testUniqueStringsNoDs(self):
        self.assertTrue(isUniqueNoDs("abcdefg"))
        self.assertTrue(isUniqueNoDs("man"))
        self.assertTrue(isUniqueNoDs(""))

    def testNonUniqueStringsNoDs(self):
        self.assertFalse(isUniqueNoDs("nascar"))
        self.assertFalse(isUniqueNoDs("mansion"))

    def testUniqueStringsBitwise(self):
        self.assertTrue(isUniqueBitwise("abcdefg"))
        self.assertTrue(isUniqueBitwise("man"))
        self.assertTrue(isUniqueBitwise(""))

    def testNonUniqueStringsBitwise(self):
        self.assertFalse(isUniqueBitwise("nascar"))
        self.assertFalse(isUniqueBitwise("mansion"))

    def testUniqueStringsSorted(self):
        self.assertTrue(is_unique_sorted("abcdefg"))
        self.assertTrue(is_unique_sorted("man"))
        self.assertTrue(is_unique_sorted(""))

    def testNonUniqueStringsSorted(self):
        self.assertFalse(is_unique_sorted("nascar"))
        self.assertFalse(is_unique_sorted("mansion"))

if __name__ == '__main__':
    unittest.main()
