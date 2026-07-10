class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return n
        summ=0
        x=[]
        for i in str(n):
            if i!='0':
                summ+=int(i)
                x.append(int(i))
        a=int("".join(map(str,x)))
        return a*summ