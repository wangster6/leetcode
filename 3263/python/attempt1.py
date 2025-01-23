"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""

class Solution:
    def toArray(self, head):
        """
        :type head: Node
        :rtype: List[int]
        """
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        return arr