# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).


def getCompression(s):  # runtime: O(n)
    compressedString = ""
    i = 0
    while (i < len(s)):
        currentCount = 1
        compressedString += s[i]
        while (i + 1 < len(s) and s[i] == s[i + 1]):
            i += 1
            currentCount += 1
        compressedString += str(currentCount)
        i += 1
    if (len(compressedString) < len(s)):
        return compressedString
    else:
        return s


def testCompression():
    assert getCompression("aabcccccaaa") == "a2b1c5a3"
    assert getCompression("aabbccdd") == "aabbccdd"
    assert getCompression("aaabbbcccddd") == "a3b3c3d3"
    assert getCompression("   ") == " 3"
    assert getCompression("abbcccc") == "a1b2c4"


def testNoCompression():
    assert getCompression("abc") == "abc"
    assert getCompression("a1b2c3") == "a1b2c3"
    assert getCompression(" ") == " "
    assert getCompression("abcccc") == "abcccc"
