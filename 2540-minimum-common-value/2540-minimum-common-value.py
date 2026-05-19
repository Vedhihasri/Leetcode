class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        a=set(nums1)&set(nums2)
        if a:
            return min(a)
        else:
            return -1






        