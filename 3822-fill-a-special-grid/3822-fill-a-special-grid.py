class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        from numpy import array, concatenate

        def dfs(n, incr):
            if n == 0:
                return array([[0]])
            incr //= 4
            upright = dfs(n - 1, incr)
            downright = upright + incr
            downleft = downright + incr
            upleft = downleft + incr
            
            return concatenate([concatenate([upleft, upright], axis = 1), concatenate([downleft, downright], axis = 1)])

        return dfs(n, (2 ** n) ** 2).tolist()