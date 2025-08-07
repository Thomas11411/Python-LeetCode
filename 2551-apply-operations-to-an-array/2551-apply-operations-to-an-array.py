class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        

        for i in range(len(nums) - 1):

            if nums[i] == nums[i + 1]:
                
                nums[i] *= 2
                nums[i + 1] = 0
                
        zero_cnt = 0
        non_zero = []

        for i in nums:
            if i != 0:
                non_zero.append(i)
            else:
                zero_cnt += 1
                
        return non_zero + [0] * zero_cnt