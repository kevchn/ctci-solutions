'''
Problem 2.6 Determine if a LinkedList is a Palindrome

September 4, 2017
Kevin Chen
'''

from datastructures import LinkedList
import unittest

def isLinkedListPalindrome(ll):
    '''
    Add first half as stack, then compare reversed first half with second half.

    time: o(n)
    space: o(n)
    where n is the # of nodes in the list

    Note: Using slow/fast pointer technique. Always lands at end of left partition.
    '''
    stack = []
    slow = fast = ll.head

    while fast and fast.next:
        stack.append(slow)
        slow = slow.next
        fast = fast.next.next
    
    # shift right partition for odd node lists
    if fast:
        slow = slow.next

    while slow:
        if stack.pop().data != slow.data:
            return False
        slow = slow.next
    
    return True


def isLinkedListPalindromeRecursive(ll):
    '''
    Recursively (recurse halfway (left), then pass down the next node (right) when recursing back through the stack)
    This is the same as creating a stack in the first half and iterating through the next and popping

    time: o(n)
    space: o(n)
    where n is the # of nodes in the list
    '''
    return recurse(ll.head, lengthOfList(ll), [None])


def recurse(head, length, node):
    if length == 1:  # odd
        node[0] = head.next
        return True
    elif length == 0:  # even
        node[0] = head
        return True

    if not recurse(head.next, length - 2, node):
        return False  # propagate Failure

    if node[0].data != head.data:
        return False

    node[0] = node[0].next
    
    return True


def lengthOfList(ll):
    count = 0
    curr = ll.head

    while curr:
        count += 1
        curr = curr.next

    return count

class Test(unittest.TestCase):
    def test_simple_one_palindrome(self):
        ll = LinkedList.LinkedList()
        ll.add_node('a')
        self.assertTrue(isLinkedListPalindrome(ll))
        self.assertTrue(isLinkedListPalindromeRecursive(ll))

    def test_simple_two_palindrome(self):
        ll = LinkedList.LinkedList()
        ll.add_node('a')
        ll.add_node('a')
        self.assertTrue(isLinkedListPalindrome(ll))
        self.assertTrue(isLinkedListPalindromeRecursive(ll))

    def test_simple_three_palindrome(self):
        ll = LinkedList.LinkedList()
        ll.add_node('a')
        ll.add_node('b')
        ll.add_node('a')
        self.assertTrue(isLinkedListPalindrome(ll))
        self.assertTrue(isLinkedListPalindromeRecursive(ll))

    def test_long_palindrome(self):
        ll = LinkedList.LinkedList()
        ll.add_node('a')
        ll.add_node('b')
        ll.add_node('b')
        ll.add_node('b')
        ll.add_node(4)
        ll.add_node('b')
        ll.add_node('b')
        ll.add_node('b')
        ll.add_node('a')
        self.assertTrue(isLinkedListPalindrome(ll))
        self.assertTrue(isLinkedListPalindromeRecursive(ll))

    def test_not_two_palindrome(self):
        ll = LinkedList.LinkedList()
        ll.add_node('a')
        ll.add_node('b')
        self.assertFalse(isLinkedListPalindrome(ll))

    def test_not_palindrome_repetition(self):
        ll = LinkedList.LinkedList()
        ll.add_node('a')
        ll.add_node('b')
        ll.add_node('a')
        ll.add_node('b')
        self.assertFalse(isLinkedListPalindrome(ll))

if __name__ == '__main__':
    unittest.main()
