class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        from math import ceil

        a3_vec = [a ** 3 for a in range(1, ceil(n ** (1/3)))]
        first, res = set(), set()

        for i, a3 in enumerate(a3_vec):
            for b3 in a3_vec[i:]:
                sum_ = a3 + b3
                if sum_ > n: break
                
                if sum_ not in first:
                    first.add(sum_)
                else:
                    res.add(sum_)
        return list(sorted(res))