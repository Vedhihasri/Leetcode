class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ar=[]
        for i in arr:
            one=bin(i).count('1')
            ar.append([one,i])
        ar.sort()
        res=[j for i,j in ar]
        return res