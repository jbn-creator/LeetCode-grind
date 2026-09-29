# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        node1 = head
        node2 = head.next
        while node2 and node2.next:
            node1 = node1.next
            node2 = node2.next.next
            if node1 == node2:
                return True
        return False
        