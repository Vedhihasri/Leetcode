class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            left=0
            right=0
            left+=sum(nums[:i])
            right+=sum(nums[i+1:])
            res.append(abs(left-right))
        return res