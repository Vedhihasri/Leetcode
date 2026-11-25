class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line=0
        weight=0
        a="abcdefghijklmnopqrstuvwxyz"
        for i in s:
            ind=a.index(i)
            weight+=widths[ind]
            if weight==100:
                line+=1
                weight=0
            elif weight>100:
                line+=1
                weight=widths[ind]
        if weight==0:
            weight=100
            line-=1
        return [line+1,weight]