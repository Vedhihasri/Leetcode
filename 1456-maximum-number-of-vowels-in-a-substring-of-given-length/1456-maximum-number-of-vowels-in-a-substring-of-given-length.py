class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel='aeiou'
        res=0
        cur_res=0
        l=0
        for i in range(k):
            if s[i] in vowel:
                cur_res+=1
        res=max(res,cur_res)
        for i in range(k,len(s)):
            if s[l] in vowel:
                cur_res-=1
            l+=1
            if s[i] in vowel:
                cur_res+=1
            res=max(res,cur_res)
        return res