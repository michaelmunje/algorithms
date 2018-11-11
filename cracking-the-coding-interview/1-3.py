# URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"


def URLify(s):  # runtime: O(n)
    outString = ""
    for i in range(len(s)):
        if s[i] != " ":
            outString += s[i]
        else:
            outString += "%20"
    return outString


def testURLify():
    assert URLify("abc cba") == "abc%20cba"
    assert URLify("Mr John Smith") == "Mr%20John%20Smith"
    assert URLify("abb ") == "abb%20"


def testURLifyNoSpaces():
    assert URLify("abc") == "abc"
    assert URLify("MrJohnSmith") == "MrJohnSmith"
