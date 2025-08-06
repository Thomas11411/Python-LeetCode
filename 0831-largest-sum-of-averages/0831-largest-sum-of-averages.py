class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        dp = [[0] * len(nums) for _ in range(k)]
        sum_ = nums.copy()

        for i,v in enumerate(sum_):
            if i == 0:
                dp[0][0] = sum_[0]
            else:
                sum_[i] += sum_[i - 1]
                dp[0][i] = sum_[i] / (i+1)

        for m in range(1,k):
            for i in range(m,len(nums)):
                for j in range(m-1,i):
                    dp[m][i] = max(dp[m][i],dp[m-1][j] + ((sum_[i] - sum_[j]) / (i - j)))

        return dp[k-1][-1]