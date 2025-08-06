class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def check(v):
            return any([v[i] > v[i + 1] for i in range(len(v) - 1)])

        cnt = 0

        while check(nums):
            min_sum = float('inf')
            
            for i in range(len(nums) - 1):
                cur_sum = nums[i] + nums[i + 1]
                if cur_sum < min_sum:
                    min_sum = cur_sum
                    idx = i
                    
            
            nums = nums[:idx] + [nums[idx] + nums[idx + 1]] + nums[idx+2:]
            cnt += 1

        return cnt