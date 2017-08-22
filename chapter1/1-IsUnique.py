'''
Problem 1.1
An algorithm to determine if a string has all unique characters

August 21, 2017
Kevin Chen
'''

import unittest

def isUnique(string):
    '''
    time: o(n)
    space: o(n)
    where n is # of chars in string
    '''
    return len(set(string)) == len(string)

def isUniqueBit(string):
    '''
    bit twiddling solution, treating 32 bit integer as 32 bit array
    does not work with characters that are not a - z

    time: o(n)
    space: o(1)
    where n is # of chars in string
    '''

    if len(string) > 26:  # pigeonhole principle
        return False

    bit_array = 0

    for char in string:
        ascii = ord(char) - ord('a')
        if bit_array & (1 << ascii) != 0:
            return False
        bit_array = bit_array | (1 << ascii)
    return True

class Test(unittest.TestCase):
    def test_unique(self):
        self.assertTrue(isUnique('abc'))
        self.assertTrue(isUniqueBit('abc'))

    def test_not_unique(self):
        self.assertFalse(isUnique('aaa'))
        self.assertFalse(isUniqueBit('aaa'))
        

    def test_not_unique_at_ends(self):
        self.assertFalse(isUnique('bab'))
        self.assertFalse(isUniqueBit('bab'))

if __name__ == '__main__':
    unittest.main()
