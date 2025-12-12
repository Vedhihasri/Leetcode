class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff=(sum(bobSizes)-sum(aliceSizes))//2 
        for i in aliceSizes:
            if i+diff in bobSizes:
                return [i,i+diff]