class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=0
        res=0
        while r<len(nums):
            if nums[r]-nums[l]==1:
                window=(r-l)+1
                res=max(res,window)
                r+=1
            elif nums[r]-nums[l]<1:
                r+=1
            else:
                l+=1
        return res