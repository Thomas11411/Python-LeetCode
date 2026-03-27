class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        idx = 0
        score = [0, 0]

        for i, v in enumerate(nums):
            
            if (v % 2) ^ ((i + 1) % 6 == 0):
                idx ^= 1
                
            score[idx] += v
        return score[0] - score[1]