# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


def getTranspose(m):
    mT = [[0 for x in range(len(m))] for y in range(len(m))]
    for i in range(len(m[0])):
        for j in range(len(m)):
            mT[i][j] = m[len(m) - 1 - j][i]
    return mT


def testTranspose():
    # m:
    #  1 4
    # -5 8
    # mT:
    # -5 1
    #  8 4
    m = [[1, 4],
         [-5, 8]]
    mT = [[-5, 1], [8, 4]]
    assert getTranspose(m) == mT
    # m:
    #  1 4 5
    # -5 8 9
    #  7 3 2
    # mT:
    #  7 -5 1
    #  3  8 4
    #  2  9 5
    m = [[1, 4, 5],
         [-5, 8, 9],
         [7, 3, 2]]
    mT = [[7, -5, 1],
          [3, 8, 4],
          [2, 9, 5]]
    assert getTranspose(m) == mT

    m = [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]
    mT = [[0, 0, 1],
          [0, 1, 0],
          [1, 0, 0]]
    assert getTranspose(m) == mT
