# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        prev=None
        while cur:
            next=cur.next
            if cur==head:
                cur.next=None
            else:
                cur.next=prev
            prev=cur
            cur=next

        return prev
        