class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count=Counter(arr)
        res=[]
        for i in count:
            if count[i]==1:
                res.append(i)
        if k <= len(res):
            return res[k - 1]
        else:
            return ""
