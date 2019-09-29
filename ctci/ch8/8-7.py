import unittest


def get_permutations(s):
    perms = []
    chosen = [False for _ in s]
    get_permutations_helper(s, len(s), chosen, [], perms)
    return perms


def get_permutations_helper(s, n, chosen, current_perm, perms):
    if len(current_perm) == n:
        perms.append(''.join(current_perm))

    for i in range(n):
        if chosen[i]:
            continue
        chosen[i] = True
        current_perm.append(s[i])
        get_permutations_helper(s, n, chosen, current_perm, perms)
        chosen[i] = False
        current_perm.pop()


class TestSolution(unittest.TestCase):
    def test_permutations(self):
        a = 'abc'
        self.assertEqual(get_permutations(a), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])


if __name__ == '__main__':
    unittest.main()
