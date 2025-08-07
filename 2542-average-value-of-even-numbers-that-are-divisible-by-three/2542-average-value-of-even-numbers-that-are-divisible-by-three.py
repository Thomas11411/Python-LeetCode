class Solution:
    def averageValue(self, nums: List[int]) -> int:
        cnt , sum_ = 0 , 0

        for i in nums:
            if i % 6 == 0:
                cnt += 1
                sum_ += i

        return int(sum_ / cnt) if cnt > 0 else 0