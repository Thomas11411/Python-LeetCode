class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
                
        res = 0

        for d in batteryPercentages:
            res += (d > res)

        return res