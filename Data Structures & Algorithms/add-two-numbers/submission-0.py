# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while curr1 or curr2:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            sumVal = val1+val2+carry
            val = sumVal % 10
            carry = sumVal //10
            curr.next = ListNode(val)
            curr = curr.next
            if curr1:
                curr1= curr1.next
            if curr2:
                curr2 = curr2.next

        if carry!=0:
            curr.next = ListNode(1)
        
        return dummy.next