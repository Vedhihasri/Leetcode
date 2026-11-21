class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        freq=Counter(tasks)
        res=0
        for i,j in freq.items():
            if j==1:
                return -1
            elif j%3==0:
                res+=(j//3)
            else:
                res+=(j//3)+1
        return res