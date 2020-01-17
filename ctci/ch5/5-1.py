import unittest


def bit_insertion(a, b, i, j):
    mask = ~0
    mask <<= j+1
    mask |= (1 << i) - 1
    return (a & mask) | (b << i)


def get_power_of_2(a):
    if a == 0:
        return -1  # so we return index from 0. problematic if we are multiplying by 0
    else:
        return 1 + get_power_of_2(a >> 1)


def multiply(a, b):
    small = min(a, b)
    big = max(a, b)
    print(small >> 1)
    out = big << get_power_of_2(small)
    print(out)
    print(get_power_of_2(small))
    for i in range(small - 2**get_power_of_2(small)):
        out += big
    return out


def isMatch(s: str, p: str) -> bool:
    def is_match_helper(word, regex):
        print(word, regex)
        nonlocal is_valid

        if not is_valid:
            if len(regex) == 0 and len(word) == 0:
                is_valid = True

            elif len(regex) > 0:

                recurse_1_1 = False
                recurse_0_2 = False
                recurse_1_0 = False

                if len(word) == 0:

                    if len(regex) > 1 and regex[0] != '*' and regex[1] == '*':
                        recurse_0_2 = True

                elif len(regex) > 1 and regex[1] == '*':
                    recurse_0_2 = True
                    if regex[0] == word[0] or regex[0] == '.':
                        recurse_1_0 = True

                elif regex[0] == '.' or regex[0] == word[0]:
                    recurse_1_1 = True

                if recurse_1_1:
                    is_match_helper(word[1:], regex[1:])

                if recurse_0_2:
                    is_match_helper(word[:], regex[2:])

                if recurse_1_0:
                    is_match_helper(word[1:], regex[:])

    is_valid = False

    is_match_helper(s, p)
    return is_valid


def get_combs(n):
    count = 0

    for i in range(n):
        for j in range(n):

            is_danger = [[False for _ in range(n)] for _ in range(n)]

            for k in range(n):
                is_danger[i][k] = True

            for k in range(n):
                is_danger[k][j] = True

            diag_i, diag_j = i, j

            while diag_i > 0 and diag_j > 0:
                diag_i -= 1
                diag_j -= 1

            while diag_i < n and diag_j < n:
                is_danger[diag_i][diag_j] = True
                diag_j += 1
                diag_i += 1

            diag_i, diag_j = i, j

            while diag_i > 0 and diag_j < n-1:
                diag_i -= 1
                diag_j += 1

            while diag_i < n and diag_j >= 0:
                is_danger[diag_i][diag_j] = True
                diag_j -= 1
                diag_i += 1

            for k in range(n):
                for l in range(n):
                    if not is_danger[k][l]:
                        count += 1

    return count / 2


class TestSolution(unittest.TestCase):
    def test_stacks(self):

        # a = 2048
        # b = 19
        # self.assertEqual(bit_insertion(a, b, 2, 6), 2124)
        #
        # a = 2057
        # b = 19
        # self.assertEqual(bit_insertion(a, b, 2, 6), 2125)
        #
        # a = 2049
        # b = 19
        # self.assertEqual(bit_insertion(a, b, 2, 6), 2125)
        #
        # a = 5
        # b = 3
        # self.assertEqual(multiply(a, b), 15)

        # a = 47
        # b = 39
        # self.assertEqual(multiply(a, b), 1833)

        #print(get_combs(3))
        #
        print(isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
        print(isMatch("aab", "c*a*b"))
        print(isMatch("bbbba", ".*a*a"))


if __name__ == '__main__':
    unittest.main()
