class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset=[]
        for i in range(len(nums)+1):
            res=list(combinations(nums,i))
            subset.extend(res)
        return subset