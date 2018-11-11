# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?


def isUnique(s):
    chars = dict()
    for i in range(len(s)):
        if s[i] in chars:
            if (chars[s[i]] == 1):
                return False
        chars[s[i]] = 1
    return True


def testUniqueStrings():
    assert isUnique("abcdefg") is True  # true
    assert isUnique("man") is True  # true
    assert isUnique("") is True


def testNonUniqueStrings():
    assert isUnique("nascar") is False  # false (palindrome)
    assert isUnique("mansion") is False  # false (n)
