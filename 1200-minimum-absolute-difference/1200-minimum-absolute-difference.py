class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res=[]
        minab=float('inf')
        for i in range(1,len(arr)):                  
            diff=arr[i]-arr[i-1]
            if diff<minab:
                minab=diff
                res=[[arr[i - 1], arr[i]]]
            elif diff==minab:
                res.append([arr[i-1],arr[i]])
        return res         