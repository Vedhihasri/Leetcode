class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums)>1:
            for i in range(len(nums)//2):
                if i%2==0:
                    nums[i]=(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    nums[i]=(max(nums[2 * i], nums[2 * i + 1]))
            nums = nums[:len(nums)//2]
        return nums[0]