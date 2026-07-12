class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a=sorted(set(arr))
        rank={i:index+1 for index,i in enumerate(a)}
        res=[]
        for i in range(len(arr)):
            res.append(rank[arr[i]])
        return res