from collections import defaultdict
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = defaultdict(int)
        for i in range(lowLimit,highLimit+1):
            count = 0
            for j in str(i):
                count += int(j)
            d[count] += 1
        return max(d.values())