class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res=[]
        for i in nums:
            if i%2==0 and i%3==0:
                res.append(i)
        if len(res)==0:
            return 0
        return int(sum(res)/len(res))