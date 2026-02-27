class Solution:
    def balancedStringSplit(self, s: str) -> int:
        inc=0
        dec=0
        count=0
        for i in s:
            if i=='L':
                inc+=1
            elif i=='R':
                dec+=1
            if inc==dec:
                count+=1
        return count
