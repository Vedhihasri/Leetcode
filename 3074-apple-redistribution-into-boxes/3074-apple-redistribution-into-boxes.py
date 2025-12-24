class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        a=sum(apple)
        capacity.sort(reverse=True)
        c=0
        for i in capacity:
            a-=i
            c+=1
            if a<=0:
                break
        return c