class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.append("inf")
        n=len(nums)
        res=[]
        start=nums[0]
        for i in range(n-1):
            if nums[i+1]!=nums[i]+1:
                if start==nums[i]:
                    res.append(str(nums[i]))
                else:
                    res.append(f'{start}->{nums[i]}')
                start=nums[i+1]
        return res
        