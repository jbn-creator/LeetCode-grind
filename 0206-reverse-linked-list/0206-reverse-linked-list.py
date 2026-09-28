# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = head
        if not head or not head.next:
            return prev
        curr = head.next
        head.next = None
        while curr.next:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        curr.next = prev
        return curr