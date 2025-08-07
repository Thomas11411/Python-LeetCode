class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        from collections import defaultdict

        d = defaultdict(int)

        for i in range(1,len(nums)):
            if nums[i - 1] == key:
                d[nums[i]] += 1

        return sorted(d.items(), key=lambda item: item[1],reverse=True)[0][0]