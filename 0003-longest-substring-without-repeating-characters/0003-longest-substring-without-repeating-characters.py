class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longg=0
        sett=set()

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            window=(r-l)+1
            longg=max(longg,window)
            sett.add(s[r])
        return longg