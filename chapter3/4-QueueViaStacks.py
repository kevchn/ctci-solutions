'''
Problem 3.4 Implement a queue using two stacks

September 9, 2017
Kevin Chen
'''

import unittest

class QueueViaStacks(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, data):
        self.stack1.append(data)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        while len(self.stack1) > 1:
            elem = self.stack1.pop()
            self.stack2.append(elem)
        if not self.stack1:
            return None
        return self.stack1.pop()

class Test(unittest.TestCase):
    def test_pop_none(self):
        ss = QueueViaStacks()
        self.assertTrue(ss.pop() == None)
        ss.push(1)
        ss.pop()
        self.assertTrue(ss.pop() == None)

    def test_push_pop_one(self):
        ss = QueueViaStacks()
        ss.push(10)
        self.assertTrue(ss.pop() == 10)

    def test_push_pop_in_order_comprehensive(self):
        ss = QueueViaStacks()
        ss.push(10)
        ss.push(11)
        ss.push(12)
        ss.push(13)
        ss.push(14)
        self.assertTrue(ss.pop() == 10)
        self.assertTrue(ss.pop() == 11)
        ss.push(15)
        ss.push(16)
        self.assertTrue(ss.pop() == 12)
        self.assertTrue(ss.pop() == 13)
        self.assertTrue(ss.pop() == 14)
        self.assertTrue(ss.pop() == 15)
        self.assertTrue(ss.pop() == 16)
        self.assertTrue(ss.pop() == None)
        ss.push(1)
        self.assertTrue(ss.pop() == 1)

if __name__ == '__main__':
    unittest.main()
