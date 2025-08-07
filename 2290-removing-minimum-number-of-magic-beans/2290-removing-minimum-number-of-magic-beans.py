class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        mx , n = 0 , len(beans)

        for i,v in enumerate(sorted(beans)):
            mx = max(mx, (n - i) * v)

        return sum(beans) - mx