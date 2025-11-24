class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        temp=x
        s=0
        while temp>0:
            get=temp%10
            s+=get
            temp//=10
        if x%s==0:
            return s
        return -1