class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        res = []
        while len(res) < k:
            count += 1
            if count not in arr:
                res.append(count)
        return res[-1]