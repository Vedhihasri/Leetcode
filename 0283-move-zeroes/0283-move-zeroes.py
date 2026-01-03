class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        lenn=len(nums)
        while i<lenn:
            if nums[i]==0:
                nums.pop(i)
                lenn-=1
                nums.append(0)
            else:
                i+=1