'''
Problem 1.6 Compress a string into repeated character format: a1b3c5

August 25, 2017
Kevin Chen
'''

import unittest

def compressString(string):
    '''
    time: o(n)
    space: o(n)
    where n is the # of chars in the string
    '''
    
    num_repetitions = 1
    p1 = 0
    string_array = []
    
    for p2 in range(1, len(string)):
        if string[p1] == string[p2]:
            num_repetitions += 1
        else:
            string_array.append(string[p1] + str(num_repetitions))
            p1 = p2  # update pointer
            num_repetitions = 1  # reset
    string_array.append(string[p1] + str(num_repetitions))

    compressed_string = ''.join(string_array)

    return compressed_string if len(compressed_string) < len(string) else string

class Test(unittest.TestCase):
    def test_no_compression(self):
        self.assertTrue(compressString('a') == 'a')

    def test_no_compression_multiple(self):
        self.assertTrue(compressString('abbb') == 'abbb')

    def test_compression_multiple(self):
        self.assertTrue(compressString('abbbb') == 'a1b4')

    def test_compression_multiple_same(self):
        self.assertTrue(compressString('aaa') == 'a3')

    def test_compression_multiple_same(self):
        self.assertTrue(compressString('aabcccccaa') == 'a2b1c5a2')

if __name__ == '__main__':
    unittest.main()
