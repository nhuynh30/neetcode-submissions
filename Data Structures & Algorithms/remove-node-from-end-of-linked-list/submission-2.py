# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0
        while curr:
            curr=curr.next
            size+=1
        if size==n:
            head=head.next
            return head
        
        
        end = size-n
        curr = head
        for i in range(end-1):
            curr = curr.next
        
        if curr.next:
            curr.next=curr.next.next
        else:
            curr.next=None

        return head