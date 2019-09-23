import unittest


def check_palindrome_perm(s):  # O(n)
    letters = dict()
    middle_found = False
    for ch in s:
        if ch.isalpha():
            if ch in letters:
                letters[ch] += 1
            else:
                letters[ch] = 1

    for letter in letters:
        if letters[letter] % 2 == 1:
            if middle_found is True:
                return False
            else:
                middle_found = True
    return True


def check_palindrome_perm_optimized(s):  # O(n)
    letters = dict()
    num_odds = 0
    for ch in s:
        if ch.isalpha():
            if ch in letters:
                letters[ch] += 1
                if letters[ch] % 2 == 0:
                    num_odds -= 1
                else:
                    num_odds += 1
            else:
                letters[ch] = 1
                num_odds += 1
    return num_odds <= 1


def check_palindrome_perm_bitwise(s):  # O(n)
    bits = 0
    for ch in s:
        if ch.isalpha():
            value = ord(ch) - ord('a')
            bits = bits ^ (1 << value)
    return (bits ** (1/2)) / 1 == (bits ** (1/2)) // 1


class TestSolution(unittest.TestCase):
    def test_pal_perm(self):
        self.assertTrue(check_palindrome_perm("tact coa"))
        self.assertTrue(check_palindrome_perm("racecar"))

    def test_no_pal_perm(self):
        self.assertFalse(check_palindrome_perm("testt"))
        self.assertFalse(check_palindrome_perm("racecarr"))

    def test_pal_perm_opt(self):
        self.assertTrue(check_palindrome_perm_optimized("tact coa"))
        self.assertTrue(check_palindrome_perm_optimized("racecar"))

    def test_no_pal_perm_opt(self):
        self.assertFalse(check_palindrome_perm_optimized("testt"))
        self.assertFalse(check_palindrome_perm_optimized("racecarr"))

    def test_pal_perm_bitwise(self):
        self.assertTrue(check_palindrome_perm_bitwise("tact coa"))
        self.assertTrue(check_palindrome_perm_bitwise("racecar"))

    def test_no_pal_perm_bitwise(self):
        self.assertFalse(check_palindrome_perm_bitwise("testt"))
        self.assertFalse(check_palindrome_perm_bitwise("racecarr"))

if __name__ == '__main__':
    unittest.main()