class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        for c,u in sorted(boxTypes,key = lambda x: [x[1],x[0]],reverse = True):
            if c <= truckSize:
                res += (c * u)
                truckSize -= c
            else:
                res += (truckSize * u)
                return res
        return res