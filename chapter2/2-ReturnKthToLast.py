'''
Problem 2.2 Return Kth to last element of a singly linked list

August 26, 2017
Kevin Chen
'''

from datastructures import LinkedList

import unittest

def returnKthToLast(ll, k):
    '''
    time: o(n)
    space: o(1)
    where n is the # of elements in the linked list
    '''

    curr_node = ll.head
    length = 0

    while curr_node:
        length += 1
        curr_node = curr_node.next

    if k < 1 or k > length:
        return None

    curr_node = ll.head
    for i in range(length - k):
        curr_node = curr_node.next
    
    return curr_node

# Can also do this with two pointers, same complexity
# One pointer moves up k, which creates a k gap. Then both move up
# 1 by 1 until the pointer reaches the end. The other pointer is at
# the kth node.

# Can also do this recursively


class Test(unittest.TestCase):
    
    def test_return_none_out_of_bounds(self):
        ll = LinkedList.LinkedList()
        self.assertTrue(str(returnKthToLast(ll, 10)) == 'None')
        self.assertTrue(str(returnKthToLast(ll, -10)) == 'None')

    def test_return_one(self):
        ll = LinkedList.LinkedList()
        ll.add_node(1)
        self.assertTrue(str(returnKthToLast(ll, 1)) == 'Node<1>')

    def test_return_all_nodes(self):
        ll = LinkedList.LinkedList()
        ll.add_node(1)
        ll.add_node(2)
        ll.add_node(3)
        # LinkedList<Node(3), Node<2>, Node<1>>
        self.assertTrue(str(returnKthToLast(ll, 1)) == 'Node<1>')
        self.assertTrue(str(returnKthToLast(ll, 2)) == 'Node<2>')
        self.assertTrue(str(returnKthToLast(ll, 3)) == 'Node<3>')

if __name__ == '__main__':
    unittest.main()
