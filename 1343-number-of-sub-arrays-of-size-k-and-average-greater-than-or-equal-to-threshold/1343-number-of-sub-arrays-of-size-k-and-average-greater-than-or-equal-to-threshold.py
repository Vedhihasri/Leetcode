class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        summ=0
        count=0
        for i in range(k):
            summ+=arr[i]
        if summ/k>=threshold:
            count+=1
        for j in range(k,len(arr)):
            summ+=arr[j]
            summ-=arr[j-k]
            if summ/k>=threshold:
                count+=1
        return count