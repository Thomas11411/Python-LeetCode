class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        pos_idx, pos_num = [], []

        for i,v in enumerate(nums):
            if v >= 0:
                pos_idx.append(i)
                pos_num.append(v)

        pos_len = len(pos_idx)
        if pos_len <= 1: return nums
        k %= pos_len
        if k == 0: return nums

        pos_num = pos_num[k:] + pos_num[:k]

        for i,v in zip(pos_idx, pos_num):
            nums[i] = v
        return nums