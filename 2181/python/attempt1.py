# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head.next
        sum = 0
        prev = None
        first = True
        while current != None:
            if current.val == 0:
                new = ListNode(sum, None)
                if first:
                    head = new
                    first = False
                else:
                    prev.next = new
                prev = new
                sum = 0

                current = current.next
            else:
                sum += current.val

                current = current.next
        
        return head