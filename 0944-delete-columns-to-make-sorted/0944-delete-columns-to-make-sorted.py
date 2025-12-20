class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        col=list(zip(*strs))
        c=0
        for i in col:
            if sorted(i)!=list(i):
                c+=1
        return c