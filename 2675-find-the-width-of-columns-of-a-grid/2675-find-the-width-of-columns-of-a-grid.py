class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [max(len(str(i)) for i in c) for c in zip(*grid)]