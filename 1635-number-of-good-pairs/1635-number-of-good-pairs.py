from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_dct = {i:v-1 for i, v in Counter(nums).items()}
        count = 0
        for i in nums_dct.values():
            if i != 0:
                count += ((1 + i) * i / 2)
        return int(count)