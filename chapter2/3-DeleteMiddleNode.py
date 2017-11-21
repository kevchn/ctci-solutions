'''
Problem 2.3 Delete a middle node, given only a reference to the node and not the list

August 26, 2017
Kevin Chen
'''

from datastructures import LinkedList

import unittest

def deleteMiddleNode(node):
    '''
    Doesn't work on last node, whereas using the previous node
    requires a head reference.

    time: o(1)
    space: o(1)
    '''
    node.data = node.next.data
    node.next = node.next.next

class Test(unittest.TestCase):
    def test_delete_middle_node(self):
        ll = LinkedList.LinkedList()
        ll.add_node(1)
        ll.add_node(2)
        ll.add_node(3)
        deleteMiddleNode(ll.head.next)
        self.assertTrue(str(ll) == 'LinkedList<Node<3>, Node<1>>')

if __name__ == '__main__':
    unittest.main()
