class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        from collections import defaultdict
        d1 = defaultdict(int)
        for i,j in edges:
            d1[i] += 1
            d1[j] += 1
        return sorted(d1.items(), key=lambda item: item[1],reverse = True)[0][0]