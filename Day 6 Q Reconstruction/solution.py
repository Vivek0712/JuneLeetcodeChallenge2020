class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = lambda x: (-x[0],x[1]) )
        sol = []
        for i in people:
            sol.insert(i[1],i)
        return sol