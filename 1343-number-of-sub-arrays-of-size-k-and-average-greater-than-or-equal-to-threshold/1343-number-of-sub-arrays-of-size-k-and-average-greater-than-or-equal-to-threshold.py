class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        summ=0
        avg=0
        for i in range(k):
            summ+=arr[i]
            avg=summ/k
        if avg>=threshold:
            count+=1

        for j in range(k,len(arr)):
            summ-=arr[j-k]
            summ+=arr[j]
            avg=summ/k
            if avg>=threshold:
                count+=1
        return count