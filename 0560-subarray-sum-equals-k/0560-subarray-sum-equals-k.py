class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={0:1}
        prefix=0
        count=0
        for i in nums:
            prefix+=i
            diff=prefix-k
            if diff in freq:
                count+=freq[diff]
            freq[prefix]=freq.get(prefix,0)+1
        return count