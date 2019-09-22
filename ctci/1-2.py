# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?


def isPermutation(s, p):  # runtime: O(n)
    chars = dict()
    chars2 = dict()
    for i in range(len(s)):
        if s[i] in chars:
            chars[s[i]] += 1
        else:
            chars[s[i]] = 1
    for i in range(len(p)):
        if p[i] in chars2:
            chars2[p[i]] += 1
        else:
            chars2[p[i]] = 1
    if (len(s) != len(p)):
        return False
    for entry in chars:
        if (entry not in chars2):
            return False
        if (chars[entry] != chars2[entry]):
            return False
    return True


def isUniqueNoDs(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


def testPermutationStrings():
    assert isPermutation("abc", "cba") is True
    assert isPermutation("abc", "acb") is True


def testNonUniqueStrings():
    assert isPermutation("abc", "cbad") is False
    assert isPermutation("abc", "abb") is False
