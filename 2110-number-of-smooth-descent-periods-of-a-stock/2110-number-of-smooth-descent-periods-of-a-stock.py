class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        c=len(prices)
        a=1
        b=1
        for i in range(1, len(prices)):
            if prices[i - 1]-prices[i]==1:
                b+=1
            else:
                b=1
            a+=b
        return a