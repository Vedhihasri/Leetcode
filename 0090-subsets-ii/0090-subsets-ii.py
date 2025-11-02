class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        for i in range(len(nums)+1):
            for k in combinations(nums, i):
                res.add(k)
        return [ list(j) for j in res]

