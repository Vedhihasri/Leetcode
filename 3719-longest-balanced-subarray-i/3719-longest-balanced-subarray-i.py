class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            even=set()
            odd=set()
            for j in range(i,len(nums)):            
                if nums[j]%2==0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])
                lenn=j-i+1  
                if len(odd)==len(even):
                    res=max(res,lenn)
        return res
