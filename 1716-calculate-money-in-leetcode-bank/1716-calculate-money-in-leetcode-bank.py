class Solution:
    def totalMoney(self, n: int) -> int:
        tot=0
        week=1
        curr=week
        for i in range(1,n+1):
            tot+=curr
            if i%7==0:
                week+=1
                curr=week
            else:
                curr+=1
        return tot