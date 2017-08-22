'''
Problem 1.2 Check if two strings are permutations of one another

August 21, 2017
Kevin Chen
'''

from collections import defaultdict
import unittest

def isPermutation(str1, str2):
    '''
    time: o(n)
    space: o(n)
    where n is # of combined chars in both strings
    '''
    return charDictFromString(str1) == charDictFromString(str2)

def charDictFromString(str):
    char_dict = defaultdict(int)
    for char in str:
        char_dict[char] += 1
    return char_dict

class Test(unittest.TestCase):
    def test_equal(self):
        self.assertTrue(isPermutation('aaa','aaa'))

    def test_permutation(self):
        self.assertTrue(isPermutation('baa','aab'))

    def test_not_permutation(self):
        self.assertFalse(isPermutation('bab','aab'))

if __name__ == '__main__':
    unittest.main()
