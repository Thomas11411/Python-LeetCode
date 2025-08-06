class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(list(map(lambda x, y: x<=queryTime<=y, startTime,endTime)))