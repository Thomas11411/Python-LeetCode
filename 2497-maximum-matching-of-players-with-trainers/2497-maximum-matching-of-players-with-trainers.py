class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        import heapq

        res = 0
        trainers.sort()
        heapq.heapify(players)

        for t in trainers:
            if players:
                if players[0] <= t:
                    heapq.heappop(players)
                    res += 1
            else:
                return res

        return res