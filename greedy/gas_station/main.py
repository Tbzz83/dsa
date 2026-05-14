'''
There are n gas stations along a circular route. You are given two integer arrays gas and cost where:

    gas[i] is the amount of gas at the ith station.
    cost[i] is the amount of gas needed to travel from the ith station to the (i + 1)th station. (The last station is connected to the first station)

You have a car that can store an unlimited amount of gas, but you begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index such that you can travel around the circuit once in the clockwise direction. If it's impossible, then return -1.

It's guaranteed that at most one solution exists.
'''

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        LENGTH = len(gas)
        # There must be a solution
        for i in range(LENGTH):
            # Try each i
            cur_gas = 0

            for j in range(i,LENGTH):
                cur_gas += gas[j] - cost[j]
                if cur_gas < 0:
                    break

            if cur_gas >= 0:
                return i

        # Case can't be reached but we'll make pyright happy
        return -1

        

def main():
    gas=[5,8,2,8]
    cost=[6,5,6,6]

    sol = Solution()
    print(sol.canCompleteCircuit(gas, cost))

if __name__ == "__main__":
    main()
