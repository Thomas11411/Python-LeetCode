class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        res = 0
        count = 0
        for i in range(int(len(arr) * 0.05),int(len(arr) * 0.95)):
            res += arr[i]
            count += 1

        return round(res / count,5)