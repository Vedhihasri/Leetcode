class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        res=0
        j=0
        for i in s:
            if j==len(g):
                break
            if i>=g[j]:
                res+=1
                j+=1
        return res