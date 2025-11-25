class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        i=0
        j=0
        m=len(nums1)
        n=len(nums2)
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        while i<m:
            res.append(nums1[i])
            i+=1
        while j<n:
            res.append(nums2[j])
            j+=1
        
        v=len(res)
        if len(res)%2==0:
            first=res[v//2]
            second=res[(v//2)-1]
            return (first+second)/2
        else: 
            return res[v//2]