class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even=(1+n)*n
        odd=n*n
        while even!=0:
            odd,even=even,odd%even
        return odd