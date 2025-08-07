class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        items = items1 + items2
        d = defaultdict(int)

        for i,v in items:
            d[i] += v

        return sorted(d.items())