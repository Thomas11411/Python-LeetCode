from collections import deque

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        d= deque(B)
        if A == B:
            return True
        for _ in range(1, len(A) + 1):
            d.rotate(1)
            if ''.join(list(d)) == A:
                return True
        return False

        