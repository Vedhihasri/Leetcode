class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        c=summ=0
        start=0
        end=len(nums)-1
        while start<end:
            summ=nums[start]+nums[end]
            if summ<target:
                c+=end-start
                start=start+1
            else:
                end=end-1
        return c