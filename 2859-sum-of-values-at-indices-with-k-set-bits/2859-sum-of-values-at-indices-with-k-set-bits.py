class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        summ=0
        for i,j in enumerate(nums):
            a=bin(i)[2:]
            if a.count('1')==k:
                summ+=j
        return summ
              