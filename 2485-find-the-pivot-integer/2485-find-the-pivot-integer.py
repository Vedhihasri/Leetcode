class Solution:
    def pivotInteger(self, n: int) -> int:
        summ=(n*(n+1))//2
        a=int(math.sqrt(summ))
        if a*a==summ:
            return a
        return -1