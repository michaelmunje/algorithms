import unittest


def isUniqueBitwise(s):
    checker = 0
    for c in s:
        val = ord(c) - ord('a')
        if checker & (1 << val) > 0:
            return False
        checker = checker | (1 << val)
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

if __name__ == '__main__':
    unittest.main()
