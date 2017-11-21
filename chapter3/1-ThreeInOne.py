#!/usr/bin/python

'''
Problem 3.1 Use an array to implement three stacks

September 8, 2017
Kevin Chen
'''

import unittest

# static solution
class threeInOne():
    '''
    Divide array into three equal array divisions.
    Create a fixed length stack in each array.

    If length is 3n, all divisions all equal.
    If length is 3n + 1, last division has one more (1 vs. 2/3 vs. 1/3).
    If length is 3n + 2, last and second to last division has one more (2 and 4/3 vs 2/3).
    '''
    def __init__(self, length):
        if length < 3:
            raise Exception("Array not large enough for three stacks")

        self.arr = [0] * length

        self.right_bound = [int(length * (1.0/3.0)) - 1, int(length * (2.0/3.0)) - 1, length - 1]
        self.left_bound = [0, self.right_bound[0] + 1, self.right_bound[1] + 1]
        self.head = [x - 1 for x in self.left_bound]

    def push(self, array_no, data):
        '''
        Pushes to array n (0, 1, 2)
        '''

        if array_no > 2 or array_no < 0:
            return False

        # stack is full
        if self.head[array_no] == self.right_bound[array_no]:
            return False
        
        # push onto stack
        self.head[array_no] += 1
        self.arr[self.head[array_no]] = data

        return True

    def pop(self, array_no):
        '''
        Pops from array n (0, 1, 2)
        '''

        if array_no > 2 or array_no < 0:
            return None

        # stack is empty
        if self.head[array_no] == self.left_bound[array_no] - 1:
            return None

        # pop from stack
        data = self.arr[self.head[array_no]]
        self.head[array_no] -= 1

        return data

    def __str__(self):
        bound_arr = [0] * len(self.arr)

        for lb in self.left_bound:
            bound_arr[lb] = 1
        for rb in self.right_bound:
            bound_arr[rb] = 9
            
        return "\nstack<" + str(self.arr) + ":" + ">"

# dynamic solution (significantly more complex)
class threeInOneDynamic():
    '''
    Use circular array to implement three stacks where empty
    space is minimized. (Actual implementation is too difficult/takes
    too long for a real 45 minute interview)
    '''
    pass

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.SOME_CONSTANT = 99

    def test_bounds_operations(self):
        t = threeInOne(9)  # stack

        for i in range(3):
            self.assertTrue(t.push(i, self.SOME_CONSTANT))

        self.assertFalse(t.push(3, self.SOME_CONSTANT))
        self.assertFalse(t.push(-1, self.SOME_CONSTANT))

    def test_max_stack(self):
        t = threeInOne(9)

        for i in range(3):
            self.assertTrue(t.push(0, self.SOME_CONSTANT))
        
        self.assertFalse(t.push(0, self.SOME_CONSTANT))

    def test_single_pop(self):
        t = threeInOne(9)

        self.assertTrue(t.push(0, self.SOME_CONSTANT))
        self.assertTrue(t.pop(0) == self.SOME_CONSTANT)

    def test_multiple_pop(self):
        t = threeInOne(9)

        self.assertTrue(t.push(0, self.SOME_CONSTANT))
        self.assertTrue(t.push(0, self.SOME_CONSTANT + 1))
        self.assertTrue(t.push(0, self.SOME_CONSTANT + 2))
        self.assertFalse(t.push(0, self.SOME_CONSTANT + 3))
        self.assertTrue(t.pop(0) == self.SOME_CONSTANT + 2)
        self.assertTrue(t.pop(0) == self.SOME_CONSTANT + 1)
        self.assertTrue(t.pop(0) == self.SOME_CONSTANT)
        self.assertTrue(t.pop(0) == None)

    def test_variable_stack_size(self):
        t = threeInOne(10)

        for i in range(3):
            self.assertTrue(t.push(0, self.SOME_CONSTANT))
        for i in range(3):
            self.assertTrue(t.push(1, self.SOME_CONSTANT))
        for i in range(4):
            self.assertTrue(t.push(2, self.SOME_CONSTANT))

        self.assertFalse(t.push(0, self.SOME_CONSTANT))
        self.assertFalse(t.push(1, self.SOME_CONSTANT))
        self.assertFalse(t.push(2, self.SOME_CONSTANT))

        t = threeInOne(11)

        for i in range(3):
            self.assertTrue(t.push(0, self.SOME_CONSTANT))
        for i in range(4):
            self.assertTrue(t.push(1, self.SOME_CONSTANT))
        for i in range(4):
            self.assertTrue(t.push(2, self.SOME_CONSTANT))

        self.assertFalse(t.push(0, self.SOME_CONSTANT))
        self.assertFalse(t.push(1, self.SOME_CONSTANT))
        self.assertFalse(t.push(2, self.SOME_CONSTANT))

    # def test_push(self):
    #     t = threeInOne(10)

    #     t.push(0, 1)
    #     print(t)
    #     t.push(0, 2)
    #     print(t)
    #     t.push(0, 3)
    #     print(t)
    #     t.push(0, 4)
    #     t.push(1,99)
    #     t.push(0, 100)
    #     t.push(2,102)
    #     print(t)
    #     t.pop(0)
    #     print(t)
    #     t.pop(0)
    #     print(t)

if __name__ == '__main__':
    unittest.main()