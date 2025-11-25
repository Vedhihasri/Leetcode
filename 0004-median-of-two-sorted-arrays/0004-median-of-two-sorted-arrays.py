class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=nums1+nums2
        a.sort()
        n=len(a)
        if len(a)%2!=0:
            return a[n // 2]
        else:
            mid1 = n // 2
            mid2 = mid1 - 1
            return (a[mid1] + a[mid2]) / 2
