class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # the gas level can never be negative
        # the overall trip final gas level cannot be negative

        start_pos = 0
        total_surplus = 0
        fuel_indicator = 0

        for i in range(len(gas)):
            fuel_indicator += gas[i] - cost[i]
            total_surplus += gas[i] - cost[i]
            if fuel_indicator < 0:
                fuel_indicator = 0
                start_pos = i + 1

        if total_surplus >= 0:
            return start_pos
        else:
            return -1
