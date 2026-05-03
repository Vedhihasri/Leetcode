class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        res=s
        if len(s)!=len(goal):
            return False
        for i in range(len(s)):
            shift=res[-1]+res[:-1]
            res=shift
            if res==goal:
                return True 
        return False 
        