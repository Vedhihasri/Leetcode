class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        res=set()
        for i in range(len(nums)-1):
            s=nums[i]+nums[i+1]
            if s in res:
                return True
            res.add(s)
        return False