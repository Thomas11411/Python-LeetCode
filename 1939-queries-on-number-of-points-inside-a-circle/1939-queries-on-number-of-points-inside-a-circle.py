class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        return [sum((x - i)**2 + (y - j)**2 <= r ** 2 for i,j in points) for x,y,r in queries]