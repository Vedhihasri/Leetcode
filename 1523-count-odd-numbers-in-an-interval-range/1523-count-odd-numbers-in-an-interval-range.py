class Solution:
    def countOdds(self, low: int, high: int) -> int:
        a=(high-low)//2
        if low%2!=0 or high%2!=0:
            a+=1
        return a