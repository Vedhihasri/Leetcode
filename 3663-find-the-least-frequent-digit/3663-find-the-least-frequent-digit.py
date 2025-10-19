class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        a=Counter(str(n))
        res=[]
        minn=min(a.values())
        for i,j in a.items():
            if j==minn:
                res.append(i)
        return int(min(res))