class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        hashmap={}
        prefix=0
        ans=float('-inf')

        for i in nums:
            if i-k in hashmap:
                ans = max(ans, prefix + i - hashmap[i-k])
            if i+k in hashmap:
                ans = max(ans, prefix + i - hashmap[i+k])
            hashmap[i] = min(hashmap.get(i, float('inf')), prefix)
            prefix+=i
        return ans if ans != float('-inf') else 0