class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        for l in range(len(nums)-2):
            Q1 = l + 1
            Q3 = len(nums)-1
            while Q1 < Q3:
                sum_ = nums[l] + nums[Q1] + nums[Q3]
                if sum_ > 0:
                    Q3 -= 1
                elif sum_ < 0:
                    Q1 += 1
                else:
                    if [nums[l] , nums[Q1] , nums[Q3]] not in res:
                        res.append([nums[l] , nums[Q1] , nums[Q3]])
                    Q3 -= 1
                    Q1 += 1
        return res