
import unittest

class LinkedList(object):
    '''
    Wrapper around node
    '''

    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_node(self, data):
        prev_node = None
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                if prev_node is None:
                    self.head = curr_node.next
                else:
                    prev_node.next = curr_node.next
                return True
            prev_node = curr_node
            curr_node = curr_node.next
        return False

    def __str__(self):
        nodes = []

        curr_node = self.head
        while curr_node:
            nodes.append(str(curr_node))
            curr_node = curr_node.next
        
        return 'LinkedList<' + ', '.join(nodes) + '>'

            
class Node(object):
    '''
    Access LinkedList through created head node.
    Solely using this implementation is dangerous because multiple objects
    could hold a reference to this Node, and if the Node changes
    the objects will point to the old head. 
    '''

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return 'Node<' + str(self.data) + '>'

class Test(unittest.TestCase):

    def test_linked_list(self):
        ll = LinkedList()
        self.assertTrue(str(ll) == 'LinkedList<>')

    def test_linked_list_add_node(self):
        ll = LinkedList()
        ll.add_node(0)
        self.assertTrue(str(ll) == 'LinkedList<Node<0>>')

    def test_linked_list_add_nodes(self):
        ll = LinkedList()
        ll.add_node(0)
        ll.add_node(1)
        self.assertTrue(str(ll) == 'LinkedList<Node<1>, Node<0>>')

    def test_linked_list_remove_nodes(self):
        ll = LinkedList()
        ll.add_node(0)
        ll.add_node(1)
        ll.add_node(2)
        ll.add_node(3)

        ll.remove_node(1)  # remove center
        self.assertTrue(str(ll) == 'LinkedList<Node<3>, Node<2>, Node<0>>')

        ll.remove_node(3)  # remove first
        self.assertTrue(str(ll) == 'LinkedList<Node<2>, Node<0>>')
    
        ll.remove_node(0)  # remove end
        self.assertTrue(str(ll) == 'LinkedList<Node<2>>')

if __name__ == '__main__':
    unittest.main()