class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        hashmap={0:-1}
        prefix=0

        for i in range(len(nums)):
            prefix+=nums[i]
            rem=prefix%k
            if rem in hashmap:
                if i-hashmap[rem]>=2:
                    return True
            else:
                hashmap[rem]=i
        return False