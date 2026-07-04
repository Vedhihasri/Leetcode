class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        summ=0
        sett=set()
        cursum=0
        
        for r in range(len(nums)):
            while nums[r] in sett:
                sett.remove(nums[l])
                cursum-=nums[l]
                l+=1
            sett.add(nums[r])
            cursum+=nums[r]
            summ=max(summ,cursum)
        return summ 