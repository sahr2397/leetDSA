class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n=len(gas)
        totalGasConsumption=0
        currGasConsumption=0
        start=0
        for i in range(n):
            totalGasConsumption+=gas[i]-cost[i]
            # print(totalGasConsumption)
            currGasConsumption+=gas[i]-cost[i]
            if currGasConsumption <0:
                start=i+1
                currGasConsumption=0

        if totalGasConsumption>=0: return start
        else: return -1
  


        