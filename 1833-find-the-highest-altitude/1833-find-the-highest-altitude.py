class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum_ = 0
        res = 0
        for i in gain:
            sum_ += i
            if sum_ > res:
                res = sum_
        return res