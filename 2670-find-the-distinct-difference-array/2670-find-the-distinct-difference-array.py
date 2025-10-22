class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            a=len(set(nums[:i+1]))
            b=len(set(nums[i+1:]))
            res.append(a-b)
        return res