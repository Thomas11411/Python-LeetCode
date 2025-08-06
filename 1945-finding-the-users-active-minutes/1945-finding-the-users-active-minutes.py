class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        from collections import defaultdict
        d1 = defaultdict(set)
        for i,v in logs:
            d1[i].add(v)
        res = [0] * k
        for i in d1.values():res[len(i)-1]+=1
        return res