class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx=minn=res=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                maxx,minn=minn,maxx
            maxx=max(nums[i],maxx*nums[i])
            minn=min(nums[i],minn*nums[i])
            res=max(res,maxx)
        return res