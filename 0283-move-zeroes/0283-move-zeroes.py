class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=len(nums)
        c=0
        ze=0
        for i in nums:
            if i!=0:
                nums[c]=i
                c+=1
            else:
                ze+=1
        for i in range(c, len(nums)):
            nums[i] = 0

