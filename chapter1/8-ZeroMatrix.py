'''
Problem 1.8 Zero out any rows or columns in a matrix containing 0

August 21, 2017
Kevin Chen
'''

import unittest

def zeroMatrix(matrix):
    '''
    time: o(n^2)
    space: o(n)
    where n is the number of elements in a row or column for a n x n matrix
    '''

    row_bools = [False] * len(matrix)
    col_bools = [False] * len(matrix[0])

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] is 0:
                row_bools[row] = True
                col_bools[col] = True

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row_bools[row] or col_bools[col]:
                matrix[row][col] = 0

    return matrix
    

class Test(unittest.TestCase):
    def test_zeroed_middle(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        zeroed_matrix = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        self.assertTrue(zeroMatrix(matrix) == zeroed_matrix)

    def test_zeroed_corner(self):
        matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 0]]
        zeroed_matrix = [[1, 1, 0], [1, 1, 0], [0, 0, 0]]
        self.assertTrue(zeroMatrix(matrix) == zeroed_matrix)

if __name__ == '__main__':
    unittest.main()
