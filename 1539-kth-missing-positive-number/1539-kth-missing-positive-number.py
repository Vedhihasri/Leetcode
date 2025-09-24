class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res=[]
        i=1
        while len(res)<k:
            if i not in arr:
                res.append(i)
            i+=1
        return res[k-1] 