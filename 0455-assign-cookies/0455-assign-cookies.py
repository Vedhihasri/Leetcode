class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        res=0
        j=0
        for i in s:
            if i>=g[j]:
                res+=1
                j+=1
                if len(g)==res:
                    break
        return res