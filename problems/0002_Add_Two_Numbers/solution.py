# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from models import ListNode


class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1=ListNode(0), l2=ListNode(0), carry=0):
        l1, l2 = self.default_node(l1), self.default_node(l2)
        val = l1.val + l2.val + carry
        node = ListNode(val % 10)
        carry = val >= 10
        if l1.next or l2.next or carry:
            node.next = self.addTwoNumbers(l1.next, l2.next, carry)
        return node

    DEFAULT_NODE = ListNode(0)

    def default_node(self, node):
        return node if node is not None else self.DEFAULT_NODE
