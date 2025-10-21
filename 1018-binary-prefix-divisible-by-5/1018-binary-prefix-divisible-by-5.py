class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res=[]
        c=0
        for i in nums:
            c=(c*2+i)%5
            res.append(c==0)
        return res