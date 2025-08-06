class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]

        l , r = 0 , len(nums)-1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                s , e = mid , mid
                while s >= 0 and nums[s] == target:
                    s -= 1
                while e <= len(nums) - 1 and nums[e] == target:
                    e += 1
                return [s+1,e-1]
        return [-1,-1]