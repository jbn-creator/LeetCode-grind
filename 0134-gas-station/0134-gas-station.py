class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        station = 0
        reserve = -1
        if sum(cost) > sum(gas):
            return -1
        
        for i in range(len(gas)):
            reserve += gas[i] - cost[i]

            if reserve < 0:
                reserve = 0
                station = (i + 1) % len(gas)
                
        return station 
        

        # if station is None:
        #     return -1

        # startStation = station
        # while reserve >= 0:
        
        #     if station == len(gas) - 1:
        #         nextIndex = 0
        #     else:
        #         nextIndex = station + 1
        #     print(f"station {station} cost to leave {cost[station]} reserve {reserve} next gas {gas[nextIndex]}")
        #     if reserve < cost[station]:
        #         return -1
        #     reserve += (gas[nextIndex] - cost[station])
        #     station = nextIndex

        #     if station == startStation:
        #         return startStation

        # return -1
