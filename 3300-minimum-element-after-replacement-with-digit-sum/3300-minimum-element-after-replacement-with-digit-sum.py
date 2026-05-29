class Solution:
    def minElement(self, nums: List[int]) -> int:
        res=[]
        for i in nums:
            a=sum(int(dig) for dig in str(i))
            res.append(a)
        return min(res)