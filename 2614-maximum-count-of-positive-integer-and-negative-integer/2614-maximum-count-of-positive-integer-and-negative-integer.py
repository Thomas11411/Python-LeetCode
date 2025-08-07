class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n_cnt , z_cnt = 0 , 0

        for i in nums:
            if i < 0:
                n_cnt += 1
            elif i == 0:
                z_cnt += 1
            else:
                return max(len(nums) - n_cnt - z_cnt,n_cnt)
            
        return max(len(nums) - n_cnt - z_cnt,n_cnt)