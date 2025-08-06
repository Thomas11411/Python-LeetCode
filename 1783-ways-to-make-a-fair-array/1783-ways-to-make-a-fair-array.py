class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        right_even , right_odd , left_even , left_odd = 0 , 0 , 0 , 0
        res = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                right_even += nums[i]
            else:
                right_odd += nums[i]


        for i in range(len(nums)):

            if i % 2 == 0:
                right_even -= nums[i]
            else:
                right_odd -= nums[i]

            if left_even + right_odd == left_odd + right_even:
                res += 1

            if i % 2 == 0:
                left_even += nums[i]
            else:
                left_odd += nums[i]

        return res