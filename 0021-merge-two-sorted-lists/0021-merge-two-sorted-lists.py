# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        curr1, curr2, tail = list1, list2, ListNode()
        curr = tail
        while curr1 or curr2:
            if curr2 is None:
                curr.next = curr1
                curr1 = curr1.next
            elif curr1 is None:
                curr.next = curr2
                curr2 = curr2.next
            elif curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next

        return tail.next
            