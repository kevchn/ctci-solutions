'''
Problem 1.5 Check if two strings are one character replacement or addition/deletion from one another

August 24, 2017
Kevin Chen
'''

import unittest

def oneAway(str1, str2):
    '''
    time: o(n)
    space: 0
    where n is the number of characters in the longer string
    '''

    if abs(len(str1) - len(str2)) > 1:
        return False

    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            if len(str1) == len(str2):
                return str1[i+1:] == str2[i+1:]
            elif len(str1) < len(str2):
                return str1[i:] == str2[i+1:]
            elif len(str1) > len(str2):
                return str1[i+1:] == str2[i:]
    
    return True  # if identical strings

class Test(unittest.TestCase):
    def test_two_additions(self):
        self.assertFalse(oneAway('stringgg', 'string'))

    def test_two_substractions(self):
        self.assertFalse(oneAway('stringgg', 'stri'))

    def test_equal(self):
        self.assertTrue(oneAway('string', 'string'))

    def test_subtraction_middle(self):
        self.assertTrue(oneAway('string', 'strig'))    

    def test_addition_middle(self):
        self.assertTrue(oneAway('string', 'striXng'))

    def test_addition_beginning(self):
        self.assertTrue(oneAway('string', 'Xstring'))

    def test_addition_end(self):
        self.assertTrue(oneAway('string', 'stringX'))

    def test_replacement_middle(self):
        self.assertTrue(oneAway('string', 'strXng'))

    def test_replacement_end(self):
        self.assertTrue(oneAway('string', 'strinX'))
    
    def test_replacement_beginning(self):
        self.assertTrue(oneAway('string', 'Xtring'))

if __name__ == '__main__':
    unittest.main()
