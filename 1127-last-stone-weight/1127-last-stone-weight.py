class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones.sort()
        while len(stones) > 1:
            heavy1 = stones.pop()
            heavy2 = stones.pop()
            stones.append(heavy1 - heavy2)
            stones.sort()
        if len(stones) == 0:return 0
        return stones[0]