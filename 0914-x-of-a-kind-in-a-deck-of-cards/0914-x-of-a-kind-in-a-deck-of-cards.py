class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck)<2:
            return False

        deck.sort()
        a=Counter(deck)
        val=list(a.values())

        for i in range(2,min(val)+1):
            if all(j%i==0 for j in val):
                return True
        return False