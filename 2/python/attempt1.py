# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1, num2 = 0, 0
        if l1.next is None:
            num1 = l1.val
        elif l2.next is None:
            num2 = l2.val
        
        str1, str2 = "", ""
        curr = l1
        while curr is not None:
            str1 += str(curr.val)
            curr = curr.next
        
        curr = l2
        while curr is not None:
            str2 += str(curr.val)
            curr = curr.next

        str1 = str1[::-1]
        num1 = int(str1)
        str2 = str2[::-1]
        num2 = int(str2)

        sum_reversed = str(num1 + num2)[::-1]

        linked_sum = ListNode(int(sum_reversed[0]), None)
        current = linked_sum
        for i in range(1, len(sum_reversed)):
            current.next = ListNode(int(sum_reversed[i]), None)
            current = current.next

        return linked_sum
            