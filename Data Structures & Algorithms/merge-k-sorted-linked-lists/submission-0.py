# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(head1, head2):
            res = ListNode(0)
            head = res
            while head1 and head2:
                if head1.val>head2.val:
                    head.next = ListNode(head2.val)
                    head2 = head2.next
                    head=head.next
                else:
                    head.next = ListNode(head1.val)
                    head1 = head1.next
                    head = head.next

            while head1:
                head.next = ListNode(head1.val)
                head1 = head1.next
                head = head.next

            while head2:
                head.next = ListNode(head2.val)
                head2 = head2.next
                head = head.next

            return res.next

        if not lists:
            return None
        res = lists[0]
        for i in range(1, len(lists)):
            res = merge(lists[i], res)

        return res



