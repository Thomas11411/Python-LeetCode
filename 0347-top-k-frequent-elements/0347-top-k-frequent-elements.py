class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        d1 = {k: v for k, v in sorted(Counter(nums).items(), key=lambda item: item[1] ,reverse=True)}
        return list(d1.keys())[:k]