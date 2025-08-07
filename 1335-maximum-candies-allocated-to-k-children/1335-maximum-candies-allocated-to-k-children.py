class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l , r = 1 , max(candies) + 1

        while l < r:
            mid = (l + r) // 2
            if sum(c // mid for c in candies) >= k:
                l = mid + 1
            else:
                r = mid

        return l - 1