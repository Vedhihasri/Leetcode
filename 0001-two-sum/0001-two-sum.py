class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        x=0
        y=0
        while x<len(nums):
            y=x+1
            while y<len(nums):
                if nums[x]+nums[y]==target:
                    res.append(x)
                    res.append(y)
                y+=1
            x+=1
        return res