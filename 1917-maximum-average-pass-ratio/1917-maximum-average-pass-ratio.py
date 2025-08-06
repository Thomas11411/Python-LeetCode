class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        import heapq
        q = [((x / y) - ((x+1)/(y+1)),x,y) for x,y in classes]
        heapq.heapify(q)
        while extraStudents > 0:
            k,i,j = heapq.heappop(q)
            extraStudents -= 1
            heapq.heappush(q,(((i+1)/(j+1)) - ((i+2)/(j+2)),i+1,j+1))
        return sum([z[1] / z[2] for z in q]) / len(q)