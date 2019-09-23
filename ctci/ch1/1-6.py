import unittest


def get_compression(chars):  # runtime: O(n)

    compressed_string = ""
    i = 0
    while i < len(chars):
        current_count = 1
        compressed_string += chars[i]
        while i + 1 < len(chars) and chars[i] == chars[i + 1]:
            i += 1
            current_count += 1
        if current_count > 1:
            compressed_string += str(current_count)
        i += 1

    if len(compressed_string) > len(chars):
        return chars
    else:
        return compressed_string


class TestSolution(unittest.TestCase):
    def test_compression(self):
        self.assertEqual(get_compression("aabcccccaaa"), "a2bc5a3")
        self.assertEqual(get_compression("aabbccdd"), "a2b2c2d2")
        self.assertEqual(get_compression("aaabbbcccddd"), "a3b3c3d3")
        self.assertEqual(get_compression("   "), " 3")
        self.assertEqual(get_compression("abbcccc"),"ab2c4")

    def test_no_compression(self):
        self.assertEqual(get_compression("abc"), "abc")
        self.assertEqual(get_compression(" "), " ")
        self.assertEqual(get_compression("abcccc"), "abc4")


if __name__ == '__main__':
    unittest.main()