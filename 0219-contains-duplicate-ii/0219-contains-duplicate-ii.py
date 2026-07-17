class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sett=set()
        for l,r in enumerate(nums):
            if r in sett:
                return True
            sett.add(r)
            if l>=k:
                sett.remove(nums[l-k])
        return False
