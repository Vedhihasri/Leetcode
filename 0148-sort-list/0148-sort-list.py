# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        cur=head
        while cur:
            res.append(cur.val)
            cur=cur.next
        res.sort()
        
        dum=ListNode(0)
        curr=dum
        for i in res:
            curr.next=ListNode(i)
            curr=curr.next
        return dum.next