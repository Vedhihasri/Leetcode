class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        longg=0
        zero=0

        for r in range(len(nums)):
            if nums[r]==0:
                zero+=1
            while zero>1:
                if nums[l]==0:
                    zero-=1
                l+=1
            longg=max(longg,(r-l)+1)
        return longg-1