class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        for i in range(1,len(arr)+1):
            before_k = min(i,k)
            mx = float("-inf")
            for j in range(1,before_k+1):
                mx = max(mx,arr[i-j])
                dp[i] = max(dp[i],dp[i-j]+j*mx)
        return dp[-1]