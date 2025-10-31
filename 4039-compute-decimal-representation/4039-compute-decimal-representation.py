class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        import collections

        res = collections.deque()
        pow10 = 1

        while n:
            n, d = divmod(n, 10)
            cur = d * pow10
            pow10 *= 10
            
            if cur == 0: continue
            res.appendleft(cur)

        return list(res)