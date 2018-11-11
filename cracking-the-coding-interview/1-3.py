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


# def URLifyInPlace(s, trueLength):
    # since this is python, strings are immutable
    # therefore i present the algorithm applicable
    # to a more suitable programming language
    # currentTrueLength = trueLength
    # for (int i = 0; i < currentTrueLength; i++)
    # {
    #    if (s[i] == " ")
    #        for (int j = currentTrueLength; j > i + 1; j--)
    #           s[j + 2] = s[j - 1]
    #        s[i] = "%"
    #        s[i + 1] = "2"
    #        s[i + 2] = "0"
    #        currentTrueLength += 3;
    # }


def testURLify():
    assert URLify("abc cba") == "abc%20cba"
    assert URLify("Mr John Smith") == "Mr%20John%20Smith"
    assert URLify("abb ") == "abb%20"


def testURLifyNoSpaces():
    assert URLify("abc") == "abc"
    assert URLify("MrJohnSmith") == "MrJohnSmith"
