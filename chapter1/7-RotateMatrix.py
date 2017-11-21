'''
Problem 1.7 Rotate n x n matrix counterclockwise in place

August 21, 2017
Kevin Chen
'''

import unittest

def rotateMatrix(matrix):
    '''
    time: o(n^2)
    space: 0
    where n is the number of elements in a row or column for a n x n matrix
    '''
    return [list(row) for row in (zip(*reversed(matrix)))]

class Test(unittest.TestCase):
    def test_rotation(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotated_matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.assertTrue(rotateMatrix(matrix) == rotated_matrix)

if __name__ == '__main__':
    unittest.main()
