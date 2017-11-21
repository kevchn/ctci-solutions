'''
Problem 2.4 Partition linked list by X, everything less than X is to the left,
everything greater than or equal to is to the right

August 26, 2017
Kevin Chen
'''

from datastructures import LinkedList
import unittest

def partition(ll, x):
    '''
    iterate through list and move elements less than x to head

    time: o(n)
    space: o(1)
    where n is the # of elements in the soul
    '''
    prev_node = None
    curr_node = ll.head

    while curr_node:
        next_node = curr_node.next  # temp
        if curr_node.data < x:
            # insert at head procedure
            if prev_node is None:
                ll.head = curr_node.next
            else:
                prev_node.next = curr_node.next
                curr_node.next = ll.head
                ll.head = curr_node
        else:
            prev_node = curr_node
        curr_node = next_node
    
    return ll

# Can also do this in O(n), c = 2, by creating two lists
# < and >=, and then constructing a new linkedlist
# using those lists

class Test(unittest.TestCase):
    def test_no_partition_moving(self):
        ll = LinkedList.LinkedList()
        ll.add_node(1)
        ll.add_node(2)
        ll.add_node(3)
        ll.add_node(4)
        self.assertTrue(str(partition(ll, 3) == 'LinkedList<Node<1>, Node<2>, Node<3>, Node<4>>'))

    def test_partition_move_one(self):
        ll = LinkedList.LinkedList()
        ll.add_node(1)
        ll.add_node(3)
        ll.add_node(2)
        ll.add_node(1)
        ll.add_node(3)
        self.assertTrue(str(partition(ll, 2) == 'LinkedList<Node<1>, Node<1>, Node<3>, Node<2>, Node<3>>'))

    def test_partition_move_all_but_one(self):
        ll = LinkedList.LinkedList()
        ll.add_node(10)
        ll.add_node(1)
        ll.add_node(2)
        ll.add_node(3)
        self.assertTrue(str(partition(ll, 10) == 'LinkedList<Node<3>, Node<2>, Node<1>, Node<10>>'))

if __name__ == '__main__':
    unittest.main()
