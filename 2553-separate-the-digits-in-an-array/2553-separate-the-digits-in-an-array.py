class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=list(map(int,"".join(map(str,nums))))
        return (res)