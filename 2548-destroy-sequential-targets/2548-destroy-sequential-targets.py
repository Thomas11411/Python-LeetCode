class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        from collections import Counter

        cnt_dict = Counter(i % space for i in nums)

        max_cnt = max(cnt_dict.values())

        return min(i for i in nums if cnt_dict[i % space] == max_cnt)