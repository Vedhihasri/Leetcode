class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return s
        res=[]
        for i in range(len(s)):
            for j in range(i,len(s)):
                a=s[i:j+1]
                if a==a[::-1]:
                    res.append(a)
        if res:
            long=max(res,key=len)
        return long