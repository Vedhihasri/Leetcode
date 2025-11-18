class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        minimum=float('inf')
        subsum=0
        while right<len(nums):
            subsum+=nums[right]
            
            while subsum>=target:
                minimum=min(minimum,right-left+1)
                subsum-=nums[left]
                left+=1
                
            right+=1
        return 0 if minimum==float('inf') else minimum