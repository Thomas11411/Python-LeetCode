class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        now = 0
        mn = 0
        mx = 0
        for i in differences:
            now += i
            mn = min(mn,now)
            mx = max(mx,now)

        return max(0, upper - lower + mn - mx + 1)