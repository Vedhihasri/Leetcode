class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        summ=float('inf')
        for i in range(1, n-1):
            for j in range(i+1, n):
                a = nums[:i]
                b = nums[i:j]
                c = nums[j:]
                summ=min(summ,a[0]+b[0]+c[0])
        return summ
                