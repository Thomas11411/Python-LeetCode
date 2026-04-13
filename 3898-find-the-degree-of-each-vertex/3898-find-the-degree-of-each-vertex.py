class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return list(map(lambda x: sum(x), matrix))
        