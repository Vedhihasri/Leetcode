class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        freq=Counter(arr)
        frequencies=sorted(freq.values(),reverse=True)
        remove=0
        c=0
        for i in frequencies:
            remove+=i
            c+=1
            if remove>=len(arr)//2:
                break
        return c