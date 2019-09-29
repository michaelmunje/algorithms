import unittest


def max_flip_sequence_optimal(a):

    prev_ones = 0
    at_ones = False
    current_ones = 0
    curr_max = 0

    for i in range(32):
        bit = a >> i & 1
        if bit == 1:
            if at_ones:
                current_ones += 1
            else:
                prev_ones = current_ones
                current_ones = 1
                at_ones = True
        else:
            if at_ones:
                if prev_ones + current_ones + 1 > curr_max:
                    curr_max = prev_ones + current_ones + 1
                at_ones = False

    if at_ones:
        if current_ones + prev_ones + 1 > curr_max:
            curr_max = prev_ones + current_ones + 1

    return curr_max


def max_flip_sequence(a):

    sequence = []
    at_ones = False
    sequence.append(0)

    for i in range(32):
        bit = a >> i & 1
        if bit == 1:
            if at_ones:
                sequence[-1] += 1
            else:
                sequence.append(1)
                at_ones = True
        else:
            if at_ones:
                sequence.append(1)
                at_ones = False
            else:
                sequence[-1] += 1

    curr_max = 0

    for i in range(2, len(sequence) - 1, 2):
        if sequence[i] == 1:
            if sequence[i-1] + sequence[i+1] + 1 > curr_max:
                curr_max = sequence[i-1] + sequence[i+1] + 1

    return curr_max


class TestSolution(unittest.TestCase):
    def test_stacks(self):

        self.assertEqual(max_flip_sequence(1775), 8)

        self.assertEqual(max_flip_sequence_optimal(1775), 8)


if __name__ == '__main__':
    unittest.main()
