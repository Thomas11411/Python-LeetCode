class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        now = set()
        now.add(0)
        count = 0
        sum_ = 0
        for i in nums:
            sum_ += i
            if sum_ - target in now:
                count += 1
                now = set()
            now.add(sum_)
        return count