# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr=[]
        curr=head
        while curr:
            arr.append(curr)
            curr=curr.next
        
        arr[k-1].val, arr[-k].val = arr[-k].val, arr[k-1].val
        return head