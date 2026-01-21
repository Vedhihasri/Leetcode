class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common=[]
        for i in list2:
            if i in list1:
                common.append(i)
        print(common)
        if len(common)==1:
            return common
        minn=float('inf')
        res=[]
        for i in common:
            summ=list1.index(i)+list2.index(i)
            if summ<minn:
                minn=summ
                res=[i]
            elif summ==minn:
                res.append(i)
        return res