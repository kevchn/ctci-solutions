'''
Problem 1.0 Check if a string is a permutation of a palindrome

August 24, 2017
Kevin Chen
'''

from collections import Counter
import unittest


def isPermutationPalindrome(string):
    '''
    time: o(n)
    space: o(n)
    where n is the # of chars in the string
    '''

    char_freq = Counter(string)

    one_odd = False
    for val in char_freq.values():
        if val % 2 == 1:
            if one_odd:
                return False
            else:
                one_odd = True
    return True

def isPermutationPalindromeCondensed(string):
    '''
    Slower than above (has to loop through everything)
    '''
    return sum(1 for val in Counter(string).values() if val % 2 == 1) <= 1


class Test(unittest.TestCase):
    def test_is_not_palindrome(self):
        self.assertFalse(isPermutationPalindrome('abc'))

    def test_is_not_palindrome_multiple_odds(self):
        self.assertFalse(isPermutationPalindrome('baaacccb'))

    def test_is_palindrome(self):
        self.assertTrue(isPermutationPalindrome('cbabc'))

    def test_is_palindrome_singular(self):
        self.assertTrue(isPermutationPalindrome('a'))

    def test_is_palindrome_repeated(self):
        self.assertTrue(isPermutationPalindrome('bbaaabb'))

    def test_is_palindrome_permutation(self):
        self.assertTrue(isPermutationPalindrome('aaaaabbbbcc'))

if __name__ == '__main__':
    unittest.main()
