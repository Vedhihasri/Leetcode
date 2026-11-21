class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def countless(target:int)->int:
            c=0
            start=0
            end=len(nums)-1
            while start<end:
                if nums[start]+nums[end]<=target:
                    c+=(end-start)
                    start+=1
                else:
                    end-=1
            return c
        return countless(upper)-countless(lower-1)
