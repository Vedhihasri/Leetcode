class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res=[0]*len(nums)
        res[0]=1
        for left in range(1,len(nums)):
            res[left]=res[left-1]*nums[left-1]
        
        right=1
        for r in range(len(nums)-1,-1,-1):
            res[r]*=right
            right*=nums[r]
        return res