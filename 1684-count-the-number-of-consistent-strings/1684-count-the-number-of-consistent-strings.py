class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        aset = set(allowed)
        for i in words:
            if all(c in aset for c in i):
                count+=1
        return count