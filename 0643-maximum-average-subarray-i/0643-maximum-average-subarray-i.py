class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res=0
        summ=0
        for i in range(k):
            summ+=nums[i]
        res=summ/k
        for j in range(k,len(nums)):
            summ = summ - nums[j-k] + nums[j]
            avgg=summ/k
            res=max(res,avgg)
        return res