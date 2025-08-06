from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        scores = {k: k * n for k, n in Counter(nums).items()}
        
        if len(scores) == 1: 
            return list(scores.values()).pop()
        
        nums = sorted(scores.keys())
        
        # index 0 for `i - 2`, `i - 1` left boundary validity.
        DP = [0] * (len(nums) + 1)
        
        prev = None
        for i, k in enumerate(sorted(nums)):
            i += 1
            currScore = scores[nums[i - 1]]
            if prev is not None and k == prev + 1:
                DP[i] = max(
                    DP[i - 2] + currScore,      # case 1. Keep the score 
                    DP[i - 1])                  # case 2. Drop the score 
            else:
                DP[i] = DP[i - 1] + currScore   # happily keep the score
            prev = k
        return DP[-1]
        