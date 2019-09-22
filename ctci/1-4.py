# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-
# drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation

# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.)


def checkPalindromePerm(s):  # runtime: O(n^2)
    letterDict = dict()
    middleFound = False
    for i in range(len(s)):
        if (s[i].isalpha()):
            if s[i] in letterDict:
                letterDict[s[i]] += 1
            else:
                letterDict[s[i]] = 1
    for letter in letterDict:
        if (letterDict[letter] % 2 == 1):
            if (middleFound is True):
                return False
            else:
                middleFound = True
    return True


def testPalPerm():
    assert checkPalindromePerm("tact coa") is True
    assert checkPalindromePerm("racecar") is True


def testNoPalPerm():
    assert checkPalindromePerm("testt") is False
    assert checkPalindromePerm("racecarr") is False
