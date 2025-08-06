class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        l = 0
        seen = set()

        for r in range(len(nums)):

            curr += nums[r]

            if nums[r] not in seen:

                res = max(res,curr)
                seen.add(nums[r])
            else:
                while nums[r] != nums[l]:
                    curr -= nums[l]
                    seen.remove(nums[l])
                    l += 1

                curr -= nums[l]
                l += 1   

        return res