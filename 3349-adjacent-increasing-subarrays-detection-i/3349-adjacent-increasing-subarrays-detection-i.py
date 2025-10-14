class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-2*k+1):
            first=nums[i:i+k] 
            second=nums[i+k:i+2*k]
            
            fi=True
            for j in range(k-1):
                if first[j]>=first[j+1]:
                    fi=False
                    break

            si=True
            for h in range(k-1):
                if second[h]>=second[h+1]:
                    si=False
                    break
            if fi and si:
                return True
        return False

