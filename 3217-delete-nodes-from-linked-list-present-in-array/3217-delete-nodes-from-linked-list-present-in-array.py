# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numset=set(nums)
        dum=ListNode(0)
        cur=dum
        while head:
            if head.val not in numset:
                cur.next=head
                cur=cur.next
            head=head.next
        cur.next = None
        return dum.next 