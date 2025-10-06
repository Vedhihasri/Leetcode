# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        cur=head.next
        summ=0
        while cur:
            if cur.val==0:
                res.append(summ)
                summ=0
            else:
                summ+=cur.val
            cur=cur.next
        dum=ListNode(0)
        curr=dum
        for i in res:
            curr.next=ListNode(i)
            curr=curr.next
        return dum.next

