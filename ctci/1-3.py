import unittest


def make_url(s):  # runtime: O(n)
    out_string = ""
    for c in s:
        if c != " ":
            out_string += c
        else:
            out_string += "%20"
    return out_string


def make_url_no_additional_memory(s):  # runtime: O(n^2)
    s = list(s)  # Since strings are immutable in python
    for i in range(len(s)):
        if s[i] == ' ':
            for j in range(1, len(s) - i - 2):
                s[-j] = s[-j-2]
            s[i] = '%'
            s[i + 1] = '2'
            s[i + 2] = '0'
    return ''.join(s)


class TestSolution(unittest.TestCase):
    def test_url(self):
        self.assertEqual(make_url("abc cba"), "abc%20cba")
        self.assertEqual(make_url("Mr John Smith"), "Mr%20John%20Smith")
        self.assertEqual(make_url("abb "), "abb%20")

    def test_url_no_spaces(self):
        self.assertEqual(make_url("abc"), "abc")
        self.assertEqual(make_url("MrJohnSmith"), "MrJohnSmith")

    def test_url_no_mem(self):
        self.assertEqual(make_url_no_additional_memory("abc cba  "), "abc%20cba")
        self.assertEqual(make_url_no_additional_memory("Mr John Smith    "), "Mr%20John%20Smith")
        self.assertEqual(make_url_no_additional_memory("abb   "), "abb%20")

    def test_url_no_spaces_no_mem(self):
        self.assertEqual(make_url_no_additional_memory("abc"), "abc")
        self.assertEqual(make_url_no_additional_memory("MrJohnSmith"), "MrJohnSmith")


if __name__ == '__main__':
    unittest.main()