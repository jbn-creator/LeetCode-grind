# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # counteer for number of visited node
        """
        while counter is not n increase the counter and always keep track of the prev node
        then set the prev node's next to be the current nodes next and return the head
        """

        prevR = None
        curr = head
        while curr:
            nextN = curr.next
            curr.next = prevR
            prevR = curr
            curr = nextN

        curr = prevR

        # reversed it - curr is the start of the reversed linkedd list (head)


        prev = curr
        # val is the new pointer of the head of the reversed list
        val = curr 
        count = 1
        while count != n:
            count += 1
            prev = curr
            curr = curr.next
        if n == 1:
            if not curr.next:
                return None
            val = val.next
        else:
            prev.next = curr.next

        # removed node

        prevRr = None
        curr = val
        while curr:
            nextN = curr.next
            curr.next = prevRr
            prevRr = curr
            curr = nextN

        curr = prevRr

        # reversed bakc to initial state
        return curr
