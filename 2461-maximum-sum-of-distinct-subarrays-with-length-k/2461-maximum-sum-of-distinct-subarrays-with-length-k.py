class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l=0
        summ=0
        currsum=0
        sett=set()

        for r in range(len(nums)):
            while nums[r] in sett:
                sett.remove(nums[l])
                currsum-=nums[l]
                l+=1
            sett.add(nums[r])
            currsum+=nums[r]

            if r-l+1 == k:
                summ=max(summ,currsum)
                currsum-=nums[l]
                sett.remove(nums[l])
                l+=1
        return summ