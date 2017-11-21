'''
Problem 3.3 Create a SetOfStacks data structure that creates new stacks upon filling
but acts as one big stack otherwise

September 9, 2017
Kevin Chen
'''

import unittest

class StackSet(object):
    '''
    time: o(1)
    space: o(n)
    where n is the number elements in the StackSet
    '''
    def __init__(self, capacity):
        self.stacks = [[]]
        self.curr_stack = 0
        self.capacity = capacity

    def push(self, data):
        if len(self.stacks[self.curr_stack]) == self.capacity:  # push into full stack
            self.curr_stack += 1
            self.stacks.append([])
        self.stacks[self.curr_stack].append(data)

    def pop(self):
        if not self.stacks[self.curr_stack]:  # pop from empty stack
            if self.curr_stack != 0:
                del self.stacks[self.curr_stack]
                self.curr_stack -= 1
            else:  # no data in StackSet
                return None
        return self.stacks[self.curr_stack].pop()


class Test(unittest.TestCase):
    def test_pop_none(self):
        ss = StackSet(1)
        self.assertTrue(ss.pop() == None)
        ss.push(1)
        ss.pop()
        self.assertTrue(ss.pop() == None)

    def test_push_pop_one(self):
        ss = StackSet(1)
        ss.push(10)
        self.assertTrue(ss.pop() == 10)

    def test_push_pop_over_boundary(self):
        ss = StackSet(2)
        ss.push(10)
        ss.push(11)
        ss.push(12)
        ss.push(13)
        ss.push(14)
        self.assertTrue(str(ss.stacks) == "[[10, 11], [12, 13], [14]]")

        self.assertTrue(ss.pop() == 14)
        self.assertTrue(str(ss.stacks) == "[[10, 11], [12, 13], []]")

        self.assertTrue(ss.pop() == 13)
        self.assertTrue(str(ss.stacks) == "[[10, 11], [12]]")




if __name__ == '__main__':
    unittest.main()
