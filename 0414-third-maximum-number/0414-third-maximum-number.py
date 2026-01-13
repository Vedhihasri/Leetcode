class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr=set(nums)
        if len(arr)<3:
            return max(arr)
        
        for i in range(2):
            arr.remove(max(arr))
        return max(arr)