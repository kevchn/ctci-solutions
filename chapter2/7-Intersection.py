'''
Problem 2.7 Find the first intersecting node between two linked lists

September 6, 2017
Kevin Chen
'''

from collections import namedtuple
from datastructures import LinkedList
import unittest

def getIntersection(list1, list2):
    '''
    Get intersection between two lists using parallel pointers.
    time: o(n)
    space: o(1)
    '''
    attr_1, attr_2 = getListAttributes(list1), getListAttributes(list2)
    
    # intersection doesn't exist
    if attr_1.tail != attr_2.tail or attr_1.size == 0 or attr_2 == 0: return None

    # pointers to variant length lists (WLOG)
    if attr_1.size <= attr_2.size:
        shorter, longer = list1.head, list2.head
    else:
        longer, shorter = list1.head, list2.head

    # make pointers parallel
    for i in range(abs(attr_1.size - attr_2.size)):
        longer = longer.next

    # get intersection
    while shorter and longer:
        if shorter is longer:
            intersection = shorter = longer
            return intersection  # WLOG

        shorter, longer = shorter.next, longer.next

    raise Exception("Tails are same but intersection not found")


def getListAttributes(l):
    '''
    Get list attributes. Attributes: size, tail. 
    time: o(n)
    space: o(1)
    '''
    ListAttributes = namedtuple('ListAttributes', ['size', 'tail'])

    # 0-sized list
    if not l.head: return ListAttributes(size=0, tail=None)

    # get size and tail
    curr = l.head
    size = 1
    while curr.next:
        size += 1
        curr = curr.next
    
    return ListAttributes(size=size, tail=curr)


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.SOME_CONSTANT = 5
        cls.intersection = LinkedList.Node("INTERSECTION")
    
    def setUp(self):
        self.ll1 = LinkedList.LinkedList()
        self.ll2 = LinkedList.LinkedList()

    def test_empty_lists(self):
        self.assertTrue(getIntersection(self.ll1, self.ll2) is None)

        self.ll1.add_node(self.SOME_CONSTANT)
        self.assertTrue(getIntersection(self.ll1, self.ll2) is None)

        self.ll1.add_node(self.SOME_CONSTANT)
        self.assertTrue(getIntersection(self.ll1, self.ll2) is None)

    def test_no_intersection(self):
        self.ll1.add_node(self.SOME_CONSTANT)
        self.ll1.add_node(self.SOME_CONSTANT)
        self.ll2.add_node(self.SOME_CONSTANT)
        self.ll2.add_node(self.SOME_CONSTANT)
        self.assertTrue(getIntersection(self.ll1, self.ll2) is None)

        self.ll1.add_node(self.SOME_CONSTANT)
        self.assertTrue(getIntersection(self.ll1, self.ll2) is None)

    def test_short_intersection_comprehensive(self):
        self.ll1.head = self.intersection
        self.ll2.head = self.intersection
        self.assertTrue(getIntersection(self.ll1, self.ll2) is self.intersection)

        self.ll2.head = LinkedList.Node('OTHER VALUE')
        self.assertFalse(getIntersection(self.ll1, self.ll2) is self.intersection)

        self.ll2.head.next = self.intersection
        self.assertTrue(getIntersection(self.ll1, self.ll2) is self.intersection)


    def test_long_intersection(self):
        self.ll1.add_node(self.SOME_CONSTANT)
        self.ll1.add_node(self.SOME_CONSTANT)
        self.ll1.add_node(self.SOME_CONSTANT)
        self.ll1.add_node(self.SOME_CONSTANT)
        self.ll1.head.next.next.next.next = self.intersection

        self.ll2.add_node(self.SOME_CONSTANT)
        self.ll2.add_node(self.SOME_CONSTANT)
        self.ll2.head.next.next = self.intersection

        self.assertTrue(getIntersection(self.ll1, self.ll2) is self.intersection)


if __name__ == '__main__':
    unittest.main()
