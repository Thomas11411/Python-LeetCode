class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        for i,v in enumerate(colors):
            if colors[0] != v: ans = max(ans,i)
            if colors[len(colors)-1] != v: ans = max(ans,len(colors)-1-i)
        return ans