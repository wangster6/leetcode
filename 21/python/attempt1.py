# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None and list2 != None:
            return list2
        elif list1 != None and list2 == None:
            return list1
        
        if list1.val < list2.val:
            list = list1
            list1 = list1.next
        else:
            list = list2
            list2 = list2.next
        
        head = list

        while list1 != None or list2 != None:
            if list1 != None and list2 == None:
                list.next = list1
                list = list.next
                list1 = list1.next
            elif list2 != None and list1 == None:
                list.next = list2
                list = list.next
                list2 = list2.next
            else:
                if list1.val < list2.val:
                    list.next = list1
                    list = list.next
                    list1 = list1.next
                else:
                    list.next = list2
                    list = list.next
                    list2 = list2.next

        return head
        