import unittest


def check_one_away(s1, s2):  # O(n)

    found_operation = False

    if abs(len(s1) - len(s2)) > 1:
        return False

    i = 0
    j = 0

    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if found_operation is True:
                return False
            found_operation = True
            if len(s1) > len(s2):
                i += 1
            elif len(s1) < len(s2):
                j += 1
        i += 1
        j += 1

    return True


class TestSolution(unittest.TestCase):
    def test_one_away(self):
        self.assertTrue(check_one_away("fake", "fare"))
        self.assertTrue(check_one_away("fare", "fare"))
        self.assertTrue(check_one_away("fare", "farer"))
        self.assertTrue(check_one_away("fare", "far"))
        self.assertTrue(check_one_away("", " "))

    def test_not_one_away(self):
        self.assertFalse(check_one_away("fare", "farthest"))
        self.assertFalse(check_one_away("fare", "fakes"))
        self.assertFalse(check_one_away("", "  "))
        self.assertFalse(check_one_away("", "fakes"))
        self.assertFalse(check_one_away("fastest", "far"))


if __name__ == '__main__':
    unittest.main()