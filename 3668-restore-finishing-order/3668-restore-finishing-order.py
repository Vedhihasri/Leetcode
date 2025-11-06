class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        a=set(friends)
        res=[]
        for i in order:
            if i in a:
                res.append(i)
        return res