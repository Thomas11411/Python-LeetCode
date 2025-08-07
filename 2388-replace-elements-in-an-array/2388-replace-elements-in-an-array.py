class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {v : i for i, v in enumerate(nums)}

        for s,e in operations:
            i = d.pop(s)
            nums[i] = e
            d[e] = i

        return nums