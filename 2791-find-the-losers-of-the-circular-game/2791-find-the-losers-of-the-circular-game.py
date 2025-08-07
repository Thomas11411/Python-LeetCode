class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:

        seen = [0] * n
        seen[0] = 1
        p = 1
        cur = 0

        while True:
            cur = (cur + p * k) % n
            if seen[cur] == 1:
                break
            seen[cur] = 1
            p += 1
            
        return [i + 1 for i in range(n) if seen[i] == 0]