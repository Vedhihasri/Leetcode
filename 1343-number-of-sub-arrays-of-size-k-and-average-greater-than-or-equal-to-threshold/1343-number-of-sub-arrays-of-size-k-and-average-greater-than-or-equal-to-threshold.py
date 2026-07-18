class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        summ=0
        avg=[]
        cur_avg=0
        for i in range(k):
            summ+=arr[i]
        if summ/k>=threshold:
            cur_avg=summ/k
            avg.append(cur_avg)
        for j in range(k,len(arr)):
            summ+=arr[j]
            summ-=arr[j-k]
            if summ/k>=threshold:
                cur_avg=summ/k
                avg.append(cur_avg)
        return len(avg)