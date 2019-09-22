# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false


def checkOneAway(s1, s2):  # runtime: O(n)
    foundOperation = False
    if (len(s1) != len(s2) and len(s1) + 1 != len(s2) and len(s1) != len(s2) + 1):
        return False
    i = 0
    for j in range(len(s2)):
        if (i >= len(s1)):
            if (foundOperation is True):
                return False
        elif (s1[i] != s2[j]):
            if (foundOperation is False):
                if (len(s1) < len(s2)):
                    i += 2
                elif (len(s1) == len(s1)):
                    i += 1
                foundOperation = True
            else:
                return False
        else:
            i += 1
    return True


def testOneAway():
    assert checkOneAway("fake", "fare") is True
    assert checkOneAway("fare", "fare") is True
    assert checkOneAway("fare", "farer") is True
    assert checkOneAway("fare", "far") is True
    assert checkOneAway("", " ") is True


def testNotOneAway():
    assert checkOneAway("fare", "farthest") is False
    assert checkOneAway("fare", "fakes") is False
    assert checkOneAway("", "  ") is False
    assert checkOneAway("", "fakes") is False
    assert checkOneAway("fastest", "far") is False
