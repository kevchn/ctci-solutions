'''
Problem 2.5 Sum two linked lists whose contents represent an integer's digits in reverse order

August 27, 2017
Kevin Chen
'''

from datastructures import LinkedList
import unittest

def sumLists(list1, list2):
    '''
    time: o(n)
    space: o(n)
    where n is the # of elements in the greater list
    '''
    curr1 = list1.head
    curr2 = list2.head
    rem = 0
    new_nodes = []

    while curr1 or curr2:
        sum = rem
        
        if curr1 is not None:
            sum += curr1.data
            curr1 = curr1.next

        if curr2 is not None:
            sum += curr2.data
            curr2 = curr2.next

        rem = sum / 10
        val = sum % 10
        
        new_nodes.append(val)

    ll = LinkedList.LinkedList()
    for new_node in reversed(new_nodes):
        ll.add_node(new_node)

    return ll


def sumListsForward(list1, list2):
    '''
    Recursive solution to forward variant of sum lists problem
    '''
    padListZeroes(list1, list2)

    ll = LinkedList.LinkedList()
    sumListsForwardHelper(list1.head, list2.head, ll)

    return ll


def sumListsForwardHelper(curr1, curr2, ll):
    if not curr1 and not curr2:
        return 0  # base case, 0 carry

    carry = sumListsForwardHelper(curr1.next, curr2.next, ll)

    # starts at bottom of list
    sum = curr1.data + curr2.data + carry
    
    val = sum % 10
    new_carry = sum / 10

    ll.add_node(val)

    return new_carry



def padListZeroes(list1, list2):
    diff = getDiff(list1, list2)

    smaller_list = list2 if diff < 0 else list1

    for i in range(abs(diff)):
        smaller_list.add_node(0)

    

def getDiff(list1, list2):

    diff = 0
    curr1, curr2 = list1.head, list2.head
    
    while curr1 or curr2:
        if curr1:
            diff += 1
            curr1 = curr1.next

        if curr2:
            diff -= 1
            curr2 = curr2.next
    
    return diff


class Test(unittest.TestCase):
    def test_addition(self):
        list1 = LinkedList.LinkedList()
        list2 = LinkedList.LinkedList()

        list1.add_node(3)
        list1.add_node(2)
        list1.add_node(1)

        list2.add_node(3)
        list2.add_node(2)
        list2.add_node(1)

        self.assertTrue(str(sumListsForward(list1, list2)) == 'LinkedList<Node<2>, Node<4>, Node<6>>')

if __name__ == '__main__':
    unittest.main()
