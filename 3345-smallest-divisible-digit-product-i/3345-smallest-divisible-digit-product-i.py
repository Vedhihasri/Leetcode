class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            prod=1
            dup=n
            while dup>0:
                prod*=dup%10
                dup//=10
            if prod%t==0:
                return n
            n+=1