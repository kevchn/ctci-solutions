'''
Problem 2.1 Remove duplicates from an unsorted linked list

August 26, 2017
Kevin Chen
'''

from datastructures import LinkedList
import unittest


def removeDups(ll):
    '''
    Remove duplicates using buffer

    time: o(n)
    space: o(n)
    where n is the # of elements in the linked list
    '''

    seen_elements = set()

    prev_node = None
    curr_node = ll.head

    while curr_node:
        if curr_node.data in seen_elements:
            # remove node
            prev_node.next = curr_node.next
        else:
            seen_elements.add(curr_node.data)
            prev_node = curr_node  # tricky, only update previous node if the curr node is not deleted
        # iterate
        curr_node = curr_node.next

    return ll

def removeDupsWithoutBuffer(ll):
    '''
    Remove duplicates without using extra space

    time: o(n^2)
    space: o(n)
    '''

    master_node = ll.head
    while master_node:
        prev_node = master_node
        curr_node = master_node.next
        while curr_node:
            if master_node.data == curr_node.data:
                # remove curr, keep prev
                prev_node.next = curr_node.next
            else:
                prev_node = curr_node
            curr_node = curr_node.next
        master_node = master_node.next
    
    return ll

class Test(unittest.TestCase):

    def test_no_removal_single(self):
        ll = LinkedList.LinkedList()
        ll.add_node(1)
        self.assertTrue(str(removeDups(ll)) == 'LinkedList<Node<1>>')
        self.assertTrue(str(removeDupsWithoutBuffer(ll)) == 'LinkedList<Node<1>>')

    def test_no_removal_multiple(self):
        ll = LinkedList.LinkedList()
        ll.add_node(1)
        ll.add_node(2)
        ll.add_node(3)
        self.assertTrue(str(removeDups(ll)) == 'LinkedList<Node<3>, Node<2>, Node<1>>')
        self.assertTrue(str(removeDupsWithoutBuffer(ll)) == 'LinkedList<Node<3>, Node<2>, Node<1>>')

    def test_duplicate_single(self):
        ll = LinkedList.LinkedList()
        ll.add_node(2)
        ll.add_node(2)
        self.assertTrue(str(removeDups(ll)) == 'LinkedList<Node<2>>')
        self.assertTrue(str(removeDupsWithoutBuffer(ll)) == 'LinkedList<Node<2>>')

    def test_duplicate_multiple(self):
        ll = LinkedList.LinkedList()
        ll.add_node(1)
        ll.add_node(1)
        ll.add_node(2)
        ll.add_node(2)
        ll.add_node(2)
        self.assertTrue(str(removeDups(ll)) == 'LinkedList<Node<2>, Node<1>>')
        self.assertTrue(str(removeDupsWithoutBuffer(ll)) == 'LinkedList<Node<2>, Node<1>>')

    def test_duplicate_mixed(self):
        ll = LinkedList.LinkedList()
        ll.add_node(1)
        ll.add_node(1)
        ll.add_node(2)
        ll.add_node(2)
        ll.add_node(1)
        ll.add_node(1)
        self.assertTrue(str(removeDups(ll)) == 'LinkedList<Node<1>, Node<2>>')
        self.assertTrue(str(removeDupsWithoutBuffer(ll)) == 'LinkedList<Node<1>, Node<2>>')

if __name__ == '__main__':
    unittest.main()
