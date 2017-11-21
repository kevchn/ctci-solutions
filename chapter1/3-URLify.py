'''
Problem 1.3 Convert all spaces in a string to '%20'

August 24, 2017
Kevin Chen
'''

import unittest

def Urlify(string, length):
    '''
    time: o(n)
    space: o(n)
    where n is # of chars in string
    '''
    return ''.join('%20' if char == ' ' else char for char in string[:length])

class Test(unittest.TestCase):
    def test_no_replace(self):
        self.assertEqual(Urlify('aaa', 3), 'aaa')

    def test_replace_space(self):
        self.assertEqual(Urlify(' ', 1), '%20')

    def test_replace_spaces(self):
        self.assertEqual(Urlify('  ', 2), '%20%20')

    def test_replace_spaces_between_chars(self):
        self.assertEqual(Urlify('a a b', 5), 'a%20a%20b')

if __name__ == '__main__':
    unittest.main()
