class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sett=set()
        for i in range(len(nums)):
            if nums[i] in sett:
                return True
            sett.add(nums[i])
            if len(sett)>k:
                sett.remove(nums[i-k])
        return False