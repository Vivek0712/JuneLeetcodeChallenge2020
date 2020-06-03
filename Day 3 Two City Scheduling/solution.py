class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:abs(x[0]-x[1]),reverse=True)
        
        cost = 0
        counta = 0
        countb =0
        n = len(costs)//2
        for i in range(2*n):
            if counta < n and countb <n:
                if(costs[i][0] < costs[i][1]):
                    counta+=1
                    cost+= costs[i][0]
                    
                else:
                    countb+=1
                    cost+= costs[i][1]
                    
            elif counta < n:
                counta+=1
                cost+= costs[i][0]
               
            else:
                countb+=1
                cost+= costs[i][1]
                
        return cost