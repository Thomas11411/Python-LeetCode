class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
                
        n = len(colors)
        colors2 = colors * 2

        res = 0

        for i in range(n):
            if colors2[i] != colors2[i + 1] and colors2[i] == colors2[i + 2]: res += 1

        return res