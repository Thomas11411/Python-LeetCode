class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
        best_inx_dct = defaultdict(lambda: float('inf'))
        i , j = 0 , 0
        cumsum = 0
        ans = float("inf")
        best = float("inf")

        while j < len(arr):

            cumsum += arr[j]

            while cumsum > target:
                cumsum -= arr[i]
                i += 1

            if cumsum == target:
                ans = min(ans,best_inx_dct[i - 1] + j - i + 1)
                best = min(best,j - i + 1)

            best_inx_dct[j] = best
            j += 1

        return ans if ans != float("inf") else -1    