class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxi=nums[0]
        mini=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            a=nums[i]
            t_maxi=max(a,maxi*a,mini*a)
            t_mini=min(a,maxi*a,mini*a)

            maxi=t_maxi
            mini=t_mini
            res=max(res,maxi)
        return res