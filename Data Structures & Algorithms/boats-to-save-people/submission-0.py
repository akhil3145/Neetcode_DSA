class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        res = 0
        l,r = 0,n-1
        while l<=r:
            remain = limit - people[r]
            r-=1
            res+=1
            if l<=r and remain>=people[l]:
                l+=1

        return res




        