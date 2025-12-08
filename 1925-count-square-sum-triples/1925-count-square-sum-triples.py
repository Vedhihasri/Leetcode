class Solution:
    def countTriples(self, n: int) -> int:
        c=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                a=i**2+j**2
                s=int(a**0.5)
                if s*s==a and s<=n:
                    c+=1
        return c 