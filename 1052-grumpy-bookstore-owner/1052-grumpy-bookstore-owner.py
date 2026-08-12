class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        a=0
        curr=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                a+=customers[i]
                
        for j in range(minutes):
            if grumpy[j]==1:
                curr+=customers[j]

        max_cur=curr
        for k in range(minutes,len(customers)):
            if grumpy[k]==1:
                curr+=customers[k]
            left=k-minutes
            if grumpy[left]==1:
                curr-=customers[left]
            max_cur=max(curr,max_cur)
        return a+max_cur