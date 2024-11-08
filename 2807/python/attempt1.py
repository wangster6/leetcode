# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current.next != None:
            prev = current
            current = current.next
            gcd = math.gcd(prev.val, current.val)
            new = ListNode(gcd)
            new.next = current
            prev.next = new
        return head