class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        l , r = sum(nums) , sum(nums)
        res = []

        l_list = [0] * len(nums)

        for j in range(len(nums)-1,-1,-1):
            l -= nums[j]
            l_list[j] = l
            

        for i in range(len(nums)):
            r -= nums[i]
            res.append(abs(l_list[i]-r))

        return res