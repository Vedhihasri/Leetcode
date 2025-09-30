class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a=bin(n)[2:]
        for i in range(len(a)-1):
            if a[i]!=a[i+1]:
                continue
            else:
                return False
                break
        return True