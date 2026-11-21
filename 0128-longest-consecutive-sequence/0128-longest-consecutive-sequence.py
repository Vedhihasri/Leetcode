class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        lenght=0
        setnums=set(nums)
        for i in setnums:
            if (i-1) not in setnums:
                longg=1
                while longg+i in setnums:
                    longg+=1
                lenght=max(longg,lenght)
        return lenght