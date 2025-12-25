class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score=sorted(score,reverse=True)
        rank={}

        for i,n in enumerate(sorted_score):
            if i==0:
                rank[n]="Gold Medal"
            elif i==1:
                rank[n]="Silver Medal"
            elif i==2:
                rank[n]="Bronze Medal"
            else:
                rank[n]=str(i+1)

        result=[]
        for a in score:
            result.append(rank[a])

        return result        



