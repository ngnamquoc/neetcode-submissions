# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev=None
        curr=head

        while(curr is not None):
            # save next
            next=curr.next
            # reverse
            curr.next=prev
            # advance
            prev=curr
            curr=next
        

        return prev
        