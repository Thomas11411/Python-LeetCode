class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = ''.join([str(ord(i) - ord('a') + 1) for i in s])
        for i in range(k):
            nums = str(sum([int(i) for i in nums]))
        return int(nums)