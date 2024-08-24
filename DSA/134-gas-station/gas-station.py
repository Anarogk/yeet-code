class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        gass = 0
        idx = 0
        for i in range(len(gas)):
            gass += gas[i] -cost[i]
            if gass<0:
                gass = 0
                idx = i+1
                print(idx)
        return idx
        
            
