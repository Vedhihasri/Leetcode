# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=set()
        dum=ListNode(0)
        cur=dum
        while head:
            if not head.val in a:
                a.add(head.val)
                cur.next=head
                cur=cur.next
            head=head.next
        cur.next = None
        return dum.next