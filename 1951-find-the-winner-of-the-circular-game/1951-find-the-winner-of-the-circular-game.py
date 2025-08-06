class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friend = list(range(1,n+1))
        start = 0
        while len(friend) > 1:
            start = (start + k - 1) % len(friend)
            del friend[start]
        return friend[0]