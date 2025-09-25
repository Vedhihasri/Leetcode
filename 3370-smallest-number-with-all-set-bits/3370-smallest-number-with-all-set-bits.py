class Solution:
    def smallestNumber(self, n: int) -> int:
        x=n
        while True:
            a=bin(x)[2:]
            if all(ch=='1' for ch in a):
                return x
            x+=1