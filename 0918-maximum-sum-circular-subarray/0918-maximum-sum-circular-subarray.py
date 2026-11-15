class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total=0
        curmax=curmin=0
        maxsum=float('-inf')
        minsum=float('inf')

        for i in nums:
            curmax=max(i,curmax+i)
            maxsum=max(curmax,maxsum)

            curmin=min(i,curmin+i)
            minsum=min(curmin,minsum)  
            total+=i
        if maxsum<0:
            return maxsum
        return max(maxsum,total-minsum)          