# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        
        curr = head
        size = 0
        while curr:
            size+=1
            curr = curr.next
        
        curr = head
        num = (size+1)//2 - 1
        for i in range(num):
            curr=curr.next

        val = curr.next
        curr.next = None
        curr = val
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        p1 = head
        p2 = prev

        while p2:
            nextp1 = p1.next
            nextp2 = p2.next
            p1.next = p2
            p2.next = nextp1
            p1 = nextp1
            p2 = nextp2

        
        
        
            
            
        