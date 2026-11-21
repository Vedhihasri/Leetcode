class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        c=0
        start=0
        end=len(people)-1
        while start<=end:
            if (people[start]+people[end])<=limit:
                start+=1
            end-=1
            c+=1
        return c