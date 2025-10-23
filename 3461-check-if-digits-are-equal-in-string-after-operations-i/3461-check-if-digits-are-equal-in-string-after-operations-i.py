class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s=[int(c) for c in s]
        while len(s)>2:
            res=[]
            for i in range(len(s)-1):
                mod=(s[i]+s[i+1])%10
                res.append(mod)
            s=res
        return s[0]==s[1]