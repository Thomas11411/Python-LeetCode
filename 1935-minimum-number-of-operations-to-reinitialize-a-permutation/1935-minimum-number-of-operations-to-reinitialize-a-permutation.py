class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        scale = perm.copy()
        res = 0
        while True:
            arr = [0] * n
            for i in perm:
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                else:
                    arr[i] = perm[n // 2 + (i - 1) // 2]

            perm = arr.copy()
            res += 1

            if scale == perm:
                return res
        
