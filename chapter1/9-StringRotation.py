'''
Problem 1.9 Determine if a string is a rotation of another string with only one call to isSubstring

August 25, 2017
Kevin Chen
'''

import unittest

def isStringRotation(str1, str2):
    '''
    time: o(n)
    size: 0
    where n is # of chars in string
    '''
    if (len(str1) != len(str2)):
        return False

    str1_rotations = str1[1:] + str1

    if str2 in str1_rotations:
        return True
    return False

class Test(unittest.TestCase):
    def test_different_words(self):
        self.assertFalse(isStringRotation('word', 'dish'))

    def test_different_lengths(self):
        self.assertFalse(isStringRotation('word', 'wordw'))

    def test_string_rotation(self):
        self.assertTrue(isStringRotation('word', 'dwor'))
        self.assertTrue(isStringRotation('word', 'rdwo'))
        self.assertTrue(isStringRotation('word', 'ordw'))
        self.assertTrue(isStringRotation('dwor', 'ordw'))
    
if __name__ == '__main__':
    unittest.main()
