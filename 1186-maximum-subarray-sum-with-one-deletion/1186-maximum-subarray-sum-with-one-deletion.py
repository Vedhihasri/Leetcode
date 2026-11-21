class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        no_delete=arr[0]
        one_delete=float("-inf")
        res=arr[0]

        for i in range(1,len(arr)):
            a=arr[i]
            one_delete=max(no_delete,one_delete+a)
            no_delete=max(a,no_delete+a)
            res=max(no_delete,one_delete,res)
        return res