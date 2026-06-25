# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prevGroup = dummy

        while True:
            kth = prevGroup
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next
            curr = prevGroup.next
            prev = groupNext

            while curr!=groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = prevGroup.next
            prevGroup.next = kth
            prevGroup = tmp


                