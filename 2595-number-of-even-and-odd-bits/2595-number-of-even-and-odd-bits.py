class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even=0
        odd=0
        a=bin(n)[2:]
        for i in range(len(a)):
            bitt=len(a)-1-i
            if a[i]=='1':
                if bitt%2==0:
                    even+=1
                else:
                    odd+=1
        return [even,odd] 