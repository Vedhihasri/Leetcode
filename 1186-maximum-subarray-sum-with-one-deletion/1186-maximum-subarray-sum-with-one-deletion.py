class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        nodelete=arr[0]
        onedele=float('-inf')
        res=arr[0]
        for i in range(1,len(arr)):
            a=arr[i]
            onedele=max(nodelete,onedele+a)
            nodelete=max(a,nodelete+a)
            res=max(nodelete,onedele,res)
        return res