class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        res=0
        x=0
        y=0
        while x<len(nums):
            y=x
            while y<len(nums):
                if abs(nums[x]-nums[y])<= min(nums[x], nums[y]):
                    xor=nums[x]^nums[y]
                    res=max(res,xor)
                y+=1
            x+=1
        return res