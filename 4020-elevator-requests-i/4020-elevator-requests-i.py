class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        requests = [0] + requests

        res = 0

        for i in range(1, len(requests)):
            res += abs(requests[i] - requests[i - 1])

        return res