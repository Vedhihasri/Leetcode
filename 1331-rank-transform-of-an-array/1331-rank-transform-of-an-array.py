class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a=sorted(set(arr))
        rank={i:index+1 for index,i in enumerate(a)}
        res=[]
        for i in arr:
            res.append(rank[i])
        return res