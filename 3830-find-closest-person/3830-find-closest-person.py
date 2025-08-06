class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dis1 = abs(x - z)
        dis2 = abs(y - z)

        if dis1 > dis2:
            return 2
        elif dis1 < dis2:
            return 1
        else:
            return 0