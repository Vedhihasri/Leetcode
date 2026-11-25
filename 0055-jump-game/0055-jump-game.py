class Solution:
    def canJump(self, nums: list[int]) -> bool:
        jump=0
        for i in nums:
            if jump<0:
                return False
            elif i>jump:
                jump=i
            jump-=1
        return True
        
