class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d=collections.defaultdict(int)
        for w in wall:
            cur=0
            for v in w:
                cur+=v
                d[cur]+=1
            d[cur]-=1
        return len(wall)-max(d.values())