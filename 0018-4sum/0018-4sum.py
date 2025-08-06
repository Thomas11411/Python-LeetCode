class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()
        for l in range(len(nums)-3):
            for r in range(len(nums)-1,l+2,-1):
                Q1 = l + 1
                Q3 = r - 1
                while Q1 < Q3:
                    sum_ = nums[l] + nums[Q1] + nums[Q3] + nums[r]
                    if sum_ > target:
                        Q3 -= 1
                    elif sum_ < target:
                        Q1 += 1
                    else:
                        res.add((nums[l] , nums[Q1] , nums[Q3] , nums[r]))
                        Q1 += 1
                        Q3 -= 1
        return res