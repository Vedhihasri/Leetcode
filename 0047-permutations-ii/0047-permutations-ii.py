class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=set()
        for i in itertools.permutations(nums):
                res.add(i) 
        return [list(j) for j in res] 