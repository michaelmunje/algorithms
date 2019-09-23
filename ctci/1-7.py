import unittest


def rotate_point_90_cc(i, j, n):  # counter-clockwise
    return n - 1 - j, i


def rotate_point_90(i, j, n):  # clockwise
    return j, n - 1 - i


def rotate_image(pixels):

    n = len(pixels)

    for i in range(n-1):
        for j in range(i, n-1-i):
            tmp = pixels[i][j]

            a1, b1 = rotate_point_90_cc(i, j, n)
            pixels[i][j] = pixels[a1][b1]

            a2, b2 = rotate_point_90_cc(a1, b1, n)
            pixels[a1][b1] = pixels[a2][b2]

            a3, b3 = rotate_point_90_cc(a2, b2, n)
            pixels[a2][b2] = pixels[a3][b3]

            pixels[a3][b3] = tmp

    return pixels


class TestSolution(unittest.TestCase):
    def test_rotation(self):
        self.assertEqual(rotate_image([[1,2,3],[4,5,6],[7,8,9]]), [[7,4,1],[8,5,2],[9,6,3]])
        self.assertEqual(rotate_image([[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]),
                         [[15, 13, 2, 5],[14, 3, 4, 1],[12, 6, 8, 9],[16, 7, 10, 11]])


if __name__ == '__main__':
    unittest.main()