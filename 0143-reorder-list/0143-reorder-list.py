# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # step 1 reverse the half of the list
        # go to mid point then do reverse
        
        # find the mid point of the linked list which is where the reversing will take place
        curr = head
        rapidCurr = head.next
        while rapidCurr and rapidCurr.next:
            curr = curr.next
            rapidCurr= rapidCurr.next.next


        
        # reverse that linked list
        prev = None
        node = curr.next
        curr.next = None
        while node:
            nextN = node.next
            node.next = prev    
            prev = node
            node = nextN

        # merge them
        Tf0 = head
        Tf1 = prev
        while Tf1:
            nextTf0 = Tf0.next
            nextTf1 = Tf1.next
            Tf0.next = Tf1
            Tf1.next = nextTf0
            Tf0 = nextTf0
            Tf1 = nextTf1

            
        

        
        