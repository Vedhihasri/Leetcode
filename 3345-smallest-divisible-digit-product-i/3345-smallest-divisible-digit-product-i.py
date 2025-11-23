class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        p=1
        while True:
            c=n
            while c>0:
                p*=c%10
                c//=10
            if p%t==0:
                return n
            p=1
            n+=1