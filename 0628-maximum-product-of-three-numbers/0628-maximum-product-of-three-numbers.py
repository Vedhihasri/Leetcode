class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1=float('-inf')
        max2=float('-inf')
        max3=float('-inf')
        min1=min2=float('inf')
        for i in nums:
            if i>max1:
                max3=max2
                max2=max1
                max1=i
            elif i>max2:
                max3=max2
                max2=i
            elif i>max3:
                max3=i
            
            if i<min1:
                min2=min1
                min1=i
            elif i<min2:
                min2=i
        a=max1*max2*max3
        b=min1*min2*max1
        return max(a,b)