class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        freq=Counter(nums)
        op=0
        for i,j in freq.items():
            if j==1:
                return -1
            elif j%3==0:
                op+=(j//3)
            else:
                op+=(j//3)+1
        return op