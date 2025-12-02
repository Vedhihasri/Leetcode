class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==0 or num==1:
            return True
        low=0
        high=num
        ans=0
        while low<=high:
            mid=(low+high)//2
            if mid*mid==num:
                return True
            elif mid*mid<num:
                low=mid+1
                ans=mid
            else:
                high=mid-1
        return ans==num