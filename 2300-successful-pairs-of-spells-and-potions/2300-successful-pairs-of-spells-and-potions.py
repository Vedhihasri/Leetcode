class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n=len(potions)
        res=[]
        for i in spells:
            need=(success+i-1)//i
            l=0
            r=n-1
            ans=n
            while l<=r:
                mid = (l + r) // 2
                if potions[mid]>=need:
                    ans=mid
                    r=mid-1
                else:
                    l=mid+1
            res.append(n-ans)
        return res