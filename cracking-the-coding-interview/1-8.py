# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to O.


def setZeroes(m):
    newM = [[1 for x in range(len(m[0]))] for y in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if (m[i][j] == 0):
                for a in range(len(m[0])):
                    newM[i][a] = 0
                    print("i, a", i, a)
                for b in range(len(m)):
                    newM[b][j] = 0
                    print("b, j", b, j)
            elif (newM[i][j] != 0):
                newM[i][j] = m[i][j]
    return newM


def testZeroes():
    # m:
    #  1 4
    # -5 8
    # mR:
    # -5 1
    #  8 4
    m = [[1, 4],
         [-5, 8]]
    mR = [[1, 4],
          [-5, 8]]
    assert setZeroes(m) == mR
    # m:
    #  1 4 5
    # -5 0 9
    #  7 3 2
    # mR:
    #  1 0 5
    #  0 0 0
    #  7 0 2
    m = [[1, 4, 5],
         [-5, 0, 9],
         [7, 3, 2]]
    mR = [[1, 0, 5],
          [0, 0, 0],
          [7, 0, 2]]
    assert setZeroes(m) == mR
    m = [[1, 7, 8],
         [-5, 0, 0],
         [7, 0, 0]]
    mR = [[1, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
    assert setZeroes(m) == mR
