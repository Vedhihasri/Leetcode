class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        c=0
        tot=sum(nums)
        l=0
        for i in range(len(nums)-1):
                l+=nums[i]
                r=tot-l
                if l%2==r%2:
                    c+=1
        return c