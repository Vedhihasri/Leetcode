class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        index=-1
        for i in range(len(nums)):
            if nums[i]==1 and index==-1:
                index=i
            elif nums[i]==1:
                if abs(index-i+1)<k:
                    return False
                index=i
        return True   
