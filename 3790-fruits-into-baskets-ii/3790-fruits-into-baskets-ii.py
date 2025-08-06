class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        for f in fruits:
            for b in baskets:
                if b >= f:
                    baskets.remove(b)
                    break
        return len(baskets)