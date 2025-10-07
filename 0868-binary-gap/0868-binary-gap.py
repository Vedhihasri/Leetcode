class Solution:
    def binaryGap(self, n: int) -> int:
        a=bin(n)[2:]
        last=-1
        maxdis=0
        for i,j in enumerate(a):
            if j=='1':
                if last!=-1:
                    dis=i-last
                    maxdis=max(maxdis,dis)
                last=i
        return maxdis