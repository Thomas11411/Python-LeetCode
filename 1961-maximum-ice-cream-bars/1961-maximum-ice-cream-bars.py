class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        for i,v in enumerate(sorted(costs)):
            if v > coins:
                return i
            coins -= v
        return len(costs)