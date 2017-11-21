'''
Problem 3.2 Create a stack that keeps the minimum

September 8, 2017
Kevin Chen
'''

import unittest
import math

class StackMin(object):
    '''
    A stack that holds the minimum (retrieved in O(1)).
    Returns infinity for minimum of empty list.

    time: o(1)
    space: o(1)
    '''
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        if not self.stack:
            self.stack.append((data, data))  # first element in stack
        else:
            self.stack.append((data, min(self.getMin(), data)))

    def pop(self):
        return self.stack.pop()[0]

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        raise IndexError("min from empty list")

class Test(unittest.TestCase):
    def test_min(self):
        stack = StackMin()

        stack.push(3)
        self.assertTrue(stack.getMin() == 3)

        stack.push(2)
        self.assertTrue(stack.getMin() == 2)

        stack.push(4)
        self.assertTrue(stack.getMin() == 2)

        stack.push(-1)
        self.assertTrue(stack.getMin() == -1)

        stack.pop()
        self.assertTrue(stack.getMin() == 2)

        stack.pop()
        self.assertTrue(stack.getMin() == 2)

        stack.pop()
        self.assertTrue(stack.getMin() == 3)

        

if __name__ == '__main__':
    unittest.main()
