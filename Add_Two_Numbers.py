# Leetcode #2
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Run Results:
# Time: 96 ms
# Memory: 13.8 MB
#

# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # use add and carry algorithm to get sums of two numbers
        l3 = None
        carry_val = 0  # carry of two number's sum
        while l1 is not None or l2 is not None or carry_val != 0:
            if l1 is None:
                v1 = 0
            else:
                v1 = l1.val
            if l2 is None:
                v2 = 0
            else:
                v2 = l2.val
            v = v1 + v2  # part of sum
            q, r = v // 10, v % 10  # q: quotient  r: remainder
            q += (r + carry_val) // 10
            r = (r + carry_val) % 10
            nd = ListNode(r)
            if l3 is None:
                l3 = nd
                l3_p = l3
            else:
                l3_p.next = nd
                l3_p = l3_p.next
            carry_val = q
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return l3