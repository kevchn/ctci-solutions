'''
Problem 2.8 Find the first node of the (only) loop in a Linked List

September 7, 2017
Kevin Chen
'''

from datastructures import LinkedList
import unittest

def getFirstLoopNode(ll):
    '''
    Find first loop node without extra space.

    Intuition:
    Find collision point.
    Find a way to measure distance to collision point.
    Find a way to measure collision to first loop node.

    Technique:
    Use slow/fast pointer technique to find collision if there is a loop.
    When slow entered loop in k distance, fast moved k distance inside loop.
    Fast moved k % loopsize distance, and is loopsize - (k % loopsize) from slow.
    Fast catches up to slow 1 node at a time, takes loopsize - (k % loopsize) to reach slow.
    Collision spot is k % loopsize nodes from entrance.
    Move slow to 0th node, it will collide with fast in k nodes to get entrance.

    time: o(n)
    space: o(1)
    '''
    
    # detect loop and get slow/fast collision
    slow = fast = ll.head
    while True:
        if not slow or not fast.next:  # no loop
            return None
        slow = slow.next  # iterate
        fast = fast.next.next
        if slow == fast:  # found collision
            break

    # get loop entrance node
    slow = ll.head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

    
# can do this in a naive o(n) space/time solution 
# by keeping set and returning first duplicate node


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.CONSTANT = 5
        cls.NODE = LinkedList.Node('LOOP')

    def setUp(self):
        self.ll = LinkedList.LinkedList()

    def test_empty_list(self):
        self.assertTrue(getFirstLoopNode(self.ll) == None)

    def test_no_loop(self):
        self.ll.add_node(self.CONSTANT)
        self.ll.add_node(self.CONSTANT + 1)
        self.ll.add_node(self.CONSTANT + 2)
        self.assertTrue(getFirstLoopNode(self.ll) == None)

    def test_circle_single_loop(self):
        self.ll.head = self.NODE
        self.ll.head.next = self.NODE
        self.assertTrue(getFirstLoopNode(self.ll) == self.NODE)

    def test_circle_multiple_loop(self):
        self.ll.head = self.NODE
        self.ll.add_node(self.CONSTANT)
        self.ll.add_node(self.CONSTANT)
        self.ll.head.next.next.next = self.NODE
        self.assertTrue(getFirstLoopNode(self.ll) == self.NODE)

    def test_delayed_single_loop(self):
        self.ll.add_node(self.CONSTANT)
        self.ll.add_node(self.CONSTANT)
        self.ll.add_node(self.CONSTANT)
        self.ll.head.next.next.next = self.NODE
        self.ll.head.next.next.next.next = self.NODE
        self.assertTrue(getFirstLoopNode(self.ll) == self.NODE)

    def test_delayed_multiple_loop(self):
        self.ll.add_node(self.CONSTANT)
        self.ll.add_node(self.CONSTANT)
        self.ll.add_node(self.CONSTANT)
        self.ll.head.next.next.next = self.NODE  # 4th
        self.ll.add_node(self.CONSTANT)
        self.ll.add_node(self.CONSTANT)
        self.ll.add_node(self.CONSTANT)
        self.ll.head.next.next.next.next.next.next.next = self.NODE  # 8th
        self.assertTrue(getFirstLoopNode(self.ll) == self.NODE)

if __name__ == '__main__':
    unittest.main()
